
"""
backtest_runner.py – Simulation multi-actifs
Exécute le backtest sur plusieurs actifs, calcule les indicateurs, génère les signaux et exporte les résultats.
"""
# === Imports et configuration du chemin ===
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from indicators.base_indicators import IndicatorModule
import time


# === Fonction de génération de données simulées ===
import yfinance as yf

assets = [
    "AAPL", "BTC-USD", "EURUSD=X", "^FCHI",  # Apple, Bitcoin, Euro/Dollar, CAC40
    "MWN", "MGC", "MCL", "MES"           # Quelques autres pour tester
]

# === Initialisation du module principal ===
indicator_global = IndicatorModule(ema_period=114, rsi_period=14, volume_ratio_thresh=1.5)

# === Backtest multi-actifs ===
results = []

for symbol in assets:
    print(f"\n=== Backtest sur {symbol} ===")
    df = yf.download(symbol, start="2020-01-01", end="2023-01-01", interval="1d")

    # Si colonnes multi-indexées, les aplatir
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0].lower() for col in df.columns]
    else:
        df.columns = [col.lower() for col in df.columns]

    print(f"📋 Colonnes avant renommage pour {symbol} :", df.columns.tolist())
    time.sleep(1)

    if df.empty:
        print(f"Aucune donnée pour {symbol}")
        continue

    df = df.rename(columns={'open': 'open', 'high': 'high', 'low': 'low', 'close': 'close', 'volume': 'volume'})
    df = df.loc[:, ~df.columns.duplicated()]
    print(f"✅ Colonnes après nettoyage pour {symbol} :", df.columns.tolist())

    indicator_local = IndicatorModule(ema_period=114, rsi_period=14, volume_ratio_thresh=1.5)
    df_ind = indicator_local.compute_indicators(df)
    df_ind = df_ind.dropna(subset=['EMA', 'RSI'])
    df_sig = indicator_local.compute_signals(df_ind)
    df_trd = indicator_local.compute_trade_management(df_sig)
    df_trd.to_csv("data/signals_AAPL.csv", index=False)
    print("✅ Fichier AAPL exporté")
    df_eval = indicator_local.evaluate_performance(df_trd)

    tp_hits = (df_eval['TradeResult'] == 'TP Hit').sum()
    sl_hits = (df_eval['TradeResult'] == 'SL Hit').sum()
    score = tp_hits * 2 - sl_hits

    results.append({
        "Asset": symbol,
        "TP": tp_hits,
        "SL": sl_hits,
        "Score": score
    })

print("📊 Colonnes de df_visu :", df_visu.columns.tolist())
print("🔍 Exemple de données :", df_visu.head())

# === Pipeline de calcul pour AAPL (visualisation + export global) ===
df_visu = yf.download("AAPL", start="2020-01-01", end="2023-01-01")
# Si colonnes multi-indexées, les aplatir
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [col[0].lower() for col in df.columns]
else:
    df.columns = [col.lower() for col in df.columns]

df_visu = df_visu.rename(columns={
    'Open': 'open',
    'High': 'high',
    'Low': 'low',
    'Close': 'close',
    'Volume': 'volume'
})

df_indicators = indicator_global.compute_indicators(df_visu)
...
df_indicators = df_indicators.dropna(subset=['EMA', 'RSI'])
df_signals = indicator.compute_signals(df_indicators)
df_trades = indicator.compute_trade_management(df_signals)

os.makedirs("data", exist_ok=True)
if not df_trades.empty:
    df_trades.to_csv("data/signaux_trading.csv", index=False)
    print("✅ Fichier signaux_trading.csv généré avec succès.")
else:
    print("⚠️ Aucun signal généré, fichier non exporté.")


# === Créer le tableau des résultatsl ===
df_results = pd.DataFrame(results)
df_results.to_csv("data/backtest_results.csv", index=False)
print("\n=== Résumé du backtest multi-actifs ===")
print(df_results)
print(df_results.sort_values(by="Score", ascending=False))

# === Pipeline de calcul ===
df_indicators = indicator.compute_indicators(df)
df_indicators = df_indicators.dropna(subset=['EMA', 'RSI'])
df_signals = indicator.compute_signals(df_indicators)
df_trades = indicator.compute_trade_management(df_signals)

# === Affichage des résultats ===
results = indicator.evaluate_performance(df_trades)
print(results['TradeResult'].value_counts())

df_trades_filtered = df_trades.dropna(subset=['SL', 'TP'])

plt.plot(df_trades_filtered.index, df_trades_filtered['SL'], label='Stop Loss', linestyle='--', color='gray')
plt.plot(df_trades_filtered.index, df_trades_filtered['TP'], label='Take Profit', linestyle='--', color='purple')


# Signaux d'achat
buy_signals = df_trades[df_trades['BuySignal']]
plt.scatter(buy_signals.index, buy_signals['close'], label='Buy', color='green', marker='^')

# Signaux de vente
sell_signals = df_trades[df_trades['SellSignal']]
plt.scatter(sell_signals.index, sell_signals['close'], label='Sell', color='red', marker='v')

# SL / TP
plt.plot(df_trades.index, df_trades['SL'], label='Stop Loss', linestyle='--', color='gray')
plt.plot(df_trades.index, df_trades['TP'], label='Take Profit', linestyle='--', color='purple')

plt.title('Signaux de trading et gestion des positions')
plt.xlabel('Date')
plt.ylabel('Prix')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === Interface utilisateur ou export des signaux ===

os.makedirs("data", exist_ok=True)
if not df_trades.empty:
    df_trades.to_csv("data/signaux_trading.csv", index=False)

# === Génération du fichier global pour Streamlit ===
df_streamlit = pd.read_csv("data/signaux_AAPL.csv")
df_streamlit.to_csv("data/signaux_trading.csv", index=False)
print("✅ Fichier signaux_trading.csv généré pour Streamlit.")
