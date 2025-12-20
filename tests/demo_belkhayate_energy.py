# -*- coding: utf-8 -*-
"""
Script de démonstration pour l'indicateur Ballistic Énergie.

Étapes:
1) Charger le CSV fourni (200 barres M15) via `load_provided_csv`.
2) Optimiser la longueur du COG parmi (14, 19, 38) et calibrer l'énergie vs colonne ENERGIE.
3) Afficher:
   - Rapport de validation (corrélation, RMSE) et comparaison COG vs références.
   - Histogramme matplotlib de l'énergie (barres vertes/rouges, ligne zéro).
4) Exécuter un backtest simple avec Backtrader:
   - Signal d'achat si ENERGY_CALIB > 0 et close > SMA(38).
   - Signal de vente si ENERGY_CALIB < 0 et close < SMA(38).
   - Gestion du risque: 1% du capital par trade en utilisant un stop basé sur ATR(14)*2.

Bibliothèques: pandas, numpy, matplotlib, backtrader.
"""

from __future__ import annotations

import os
import sys
from typing import Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import backtrader as bt

# Import du module indicateur
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from indicators.phoebus_energy import (
    load_provided_csv,
    grid_search_energy,
    plot_energy_histogram,
    validation_report,
)


# -----------------------------
# Backtrader: DataFeed avec colonne d'énergie
# -----------------------------

class PandasDataWithEnergy(bt.feeds.PandasData):
    lines = ('energy',)
    params = (
        ('datetime', None),  # l'index datetime du DataFrame
        ('open', 'OPEN'),
        ('high', 'HIGH'),
        ('low', 'LOW'),
        ('close', 'CLOSE'),
        ('volume', None),  # volume classique absent/optionnel ici
        ('openinterest', None),
        ('energy', 'ENERGY_CALIB'),
    )


# -----------------------------
# Stratégie
# -----------------------------

class EnergyTrendStrategy(bt.Strategy):
    params = dict(
        sma_period=38,
        atr_period=14,
        atr_mult=2.0,
        risk_perc=0.01,  # 1% de risque par trade
    )

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.p.sma_period)
        self.atr = bt.indicators.ATR(self.data, period=self.p.atr_period)
        # accéder à la ligne custom energy
        self.energy = self.data.energy

    def next(self):
        if np.isnan(self.energy[0]) or np.isnan(self.sma[0]) or np.isnan(self.atr[0]):
            return

        pos = self.getposition()
        cash = self.broker.getcash()
        value = self.broker.getvalue()

        # taille basée sur un stop ATR
        atr_stop = max(1e-6, float(self.atr[0] * self.p.atr_mult))
        risk_amount = value * self.p.risk_perc
        size = 0

        if atr_stop > 0:
            size = int(max(0, risk_amount / atr_stop))

        # Conditions
        long_signal = (self.energy[0] > 0.0) and (self.data.close[0] > self.sma[0])
        short_signal = (self.energy[0] < 0.0) and (self.data.close[0] < self.sma[0])

        if not pos:
            if long_signal and size > 0:
                self.buy(size=size)
            elif short_signal and size > 0:
                self.sell(size=size)
        else:
            # sortie si signal contraire
            if pos.size > 0 and short_signal:
                self.close()
            elif pos.size < 0 and long_signal:
                self.close()


# -----------------------------
# Utilitaire de backtest
# -----------------------------

def run_backtest(df: pd.DataFrame, plot: bool = True):
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100000.0)
    cerebro.broker.setcommission(commission=0.0002)  # 2 bps par exemple

    datafeed = PandasDataWithEnergy(dataname=df)
    cerebro.adddata(datafeed)

    cerebro.addstrategy(EnergyTrendStrategy)

    # Analyzer de performance simple
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='ta')
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe', timeframe=bt.TimeFrame.Minutes, compression=15)

    results = cerebro.run()
    strat = results[0]

    ta = strat.analyzers.ta.get_analysis()
    sharpe = strat.analyzers.sharpe.get_analysis()

    print("\n===== RÉSULTATS BACKTEST =====")
    print(f"Valeur finale: {cerebro.broker.getvalue():.2f}")
    print("TradeAnalyzer:", ta)
    print("Sharpe:", sharpe)

    if plot:
        # Affiche le graphe backtrader
        cerebro.plot(iplot=False)


# -----------------------------
# Main
# -----------------------------

def main(csv_path: Optional[str] = None) -> None:
    # Emplacements possibles du CSV dans le repo
    candidates = [
        csv_path,
        os.path.join(ROOT_DIR, 'data', '200 DATA CLONE ENERGIE BGC TICK.csv'),
        os.path.join(ROOT_DIR, 'data', '200_DATA_CLONE_B_ENERGIE.csv'),
    ]
    csv_to_use = None
    for p in candidates:
        if p and os.path.exists(p):
            csv_to_use = p
            break
    if not csv_to_use:
        raise FileNotFoundError("CSV introuvable. Placez le fichier dans data/.")

    print(f"Chargement CSV: {csv_to_use}")
    df = load_provided_csv(csv_to_use)

    # Optimisation simple: on peut tester notre COG calculé ou utiliser la référence Ninjatrader
    use_ref = 'BGC Ninjatrader Calcule a la fermeture de la barre' if 'BGC Ninjatrader Calcule a la fermeture de la barre' in df.columns else None

    df_best, report = grid_search_energy(df, lengths=(14, 19, 38), use_reference_bgc=use_ref)

    print("\n===== RAPPORT VALIDATION =====")
    print(f"Meilleure longueur: {report.get('length')}")
    print(f"Corrélation énergie vs ENERGIE: {report.get('corr'):.4f}")
    print(f"RMSE énergie vs ENERGIE: {report.get('rmse'):.4f}")
    print(f"Régression: a={report.get('a'):.4f}, b={report.get('b'):.4f}")

    # Rapport détaillé (COG vs réf)
    detailed = validation_report(df, length=int(report.get('length', 19)), use_reference_bgc=use_ref)
    print("\nComparaison COG vs références:")
    for k, v in detailed.get('cogs', {}).items():
        print(f"- {k}: RMSE={v['rmse']:.5f}, Corr={v['corr']:.5f}")

    # Histogramme énergie
    print("\nAffichage de l'histogramme d'énergie...")
    plot_energy_histogram(df_best, energy_col='ENERGY_CALIB', title='Ballistic Énergie (calibrée)')

    # Superposer signaux buy/sell simples
    energy = df_best['ENERGY_CALIB'].astype(float)
    close = df_best['CLOSE'].astype(float)
    sma38 = close.rolling(38).mean()

    idx = np.arange(len(close))
    buys = (energy > 0) & (close > sma38)
    sells = (energy < 0) & (close < sma38)

    ax2 = plt.twinx()
    ax2.plot(idx, close.values, color='steelblue', label='Close')
    ax2.plot(idx, sma38.values, color='orange', label='SMA 38')
    ax2.scatter(idx[buys], close.values[buys], marker='^', color='green', label='Buy', zorder=5)
    ax2.scatter(idx[sells], close.values[sells], marker='v', color='red', label='Sell', zorder=5)
    ax2.legend(loc='upper left')

    plt.tight_layout()
    plt.show()

    # Backtest
    # Prépare DataFrame pour Backtrader (il attend un index datetime croissant)
    bt_df = df_best.copy()
    bt_df = bt_df.dropna(subset=['OPEN', 'HIGH', 'LOW', 'CLOSE', 'ENERGY_CALIB'])
    # S'assurer que l'index est de type datetime et trié
    if not isinstance(bt_df.index, pd.DatetimeIndex):
        # tenter de reconstruire si nécessaire
        if {'DATE', 'HEURE UTC+2'}.issubset(set(df_best.columns)):
            dt = pd.to_datetime(df_best['DATE'].astype(str) + ' ' + df_best['HEURE UTC+2'].astype(str), dayfirst=True, errors='coerce')
            bt_df.index = dt
    bt_df = bt_df.sort_index()

    print("\nLancement du backtest...")
    run_backtest(bt_df, plot=True)


if __name__ == "__main__":
    main()
