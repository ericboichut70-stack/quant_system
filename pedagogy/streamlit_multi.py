# === Imports et configuration du chemin ===
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from indicators.base_indicators import IndicatorModule
import time
from strategy.signal_filter import filter_signals
from indicators.phoebus_energy import grid_search_energy, plot_energy_histogram
from modules.optimizer import optimize_parameters

# === Fonction de génération de données simulées ===
import yfinance as yf

assets = [
    "AAPL", "BTC-USD", "EURUSD=X", "^FCHI",  # Apple, Bitcoin, Euro/Dollar, CAC40
    "MWN", "MGC", "MCL", "MES"           # Quelques autres pour tester
]

# === Initialisation du module ===
indicator = IndicatorModule(ema_period=114, rsi_period=14, volume_ratio_thresh=1.5)

# === Backtest multi-actifs ===
results = []

for symbol in assets:
    print(f"\n=== Backtest sur {symbol} ===")
    df = yf.download(symbol, start="2020-01-01", end="2023-01-01", interval="1d")
    time.sleep(1)  # ← ralentit la requête pour éviter les blocages
    if df.empty:
        print(f"Aucune donnée pour {symbol}")
        continue

    df = df.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'})
    indicator = IndicatorModule(ema_period=20, rsi_period=14, volume_ratio_thresh=1.5)
    df_visu = yf.download("AAPL", start="2020-01-01", end="2023-01-01")
    df_visu = df_visu.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'})
    df_indicators = indicator.compute_indicators(df_visu)
    df_indicators = df_indicators.dropna(subset=['EMA', 'RSI'])
    df_signals = indicator.compute_signals(df_indicators)
    df_trades = indicator.compute_trade_management(df_signals)

    df_ind = df_ind.dropna(subset=['EMA', 'RSI'])
    df_sig = indicator.compute_signals(df_ind)
    df_trd = indicator.compute_trade_management(df_sig)
    df_eval = indicator.evaluate_performance(df_trd)

    tp_hits = (df_eval['TradeResult'] == 'TP Hit').sum()
    sl_hits = (df_eval['TradeResult'] == 'SL Hit').sum()
    score = tp_hits * 2 - sl_hits

    results.append({
        "Asset": symbol,
        "TP": tp_hits,
        "SL": sl_hits,
        "Score": score
    })

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

# === Définition d'une fonction d'objectif ===
import optuna

def objective(trial):
    ema = trial.suggest_int("ema", 10, 200)
    rsi = trial.suggest_int("rsi", 10, 30)
    volume_thresh = trial.suggest_float("volume_ratio", 1.0, 3.0)
    sl = trial.suggest_float("sl_pct", 0.5, 3.0)
    tp = trial.suggest_float("tp_pct", 1.0, 5.0)

    df_optuna = yf.download("AAPL", start="2020-01-01", end="2023-01-01")
    df_optuna = df_optuna.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'})

    indicator = IndicatorModule(ema, rsi, volume_thresh)
    df_ind = indicator.compute_indicators(df_optuna)
    df_sig = indicator.compute_signals(df_ind)
    df_trd = indicator.compute_trade_management(df_sig, trail_pct=1.0, sl_pct=sl, tp_pct=tp)
    df_eval = indicator.evaluate_performance(df_trd)

    score = (
        (df_eval['TradeResult'] == 'TP Hit').sum() * 2
        - (df_eval['TradeResult'] == 'SL Hit').sum()
        + df_eval['ScoreIA'].mean() * 0.1
    )
    return score

# Optimisation
study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=50)
print(study.best_params)

# === Interface utilisateur ou export des signaux ===
import streamlit as st

st.title("BOT IA – Signaux de trading")
st.dataframe(df_trades[['close', 'BuySignal', 'SellSignal', 'ScoreIA', 'TrailStop', 'SL', 'TP']])

os.makedirs("data", exist_ok=True)
df_trades.to_csv("signaux_trading.csv")

# === Simuler la réaction aux news et turbulences ===
news_path = "data/news_calendar/forexfactory_impact.csv"
impact_level = "high"
window_minutes = 30
turbulence_threshold = 0.02

if st.checkbox("🧪 Simuler la réaction aux news et turbulences"):
    df["timestamp"] = pd.to_datetime(df.index)  # Assure que timestamp est bien présent
    filtered_df = filter_signals(df, news_path, impact_level, window_minutes, turbulence_threshold)
    df_alerts = filtered_df[filtered_df["reason"] != ""]
    st.warning(f"{len(df_alerts)} signaux filtrés pour cause de news ou turbulence.")
    st.dataframe(df_alerts[["timestamp", "reason", "close"]])
    if not df_alerts.empty:
        reasons = df_alerts["reason"].value_counts()
        for reason, count in reasons.items():
            st.warning(f"{count} signaux filtrés pour : {reason}")


os.makedirs("data/logs", exist_ok=True)
filtered_df.to_csv("data/logs/filtered_signals_log.csv", index=False)

from strategy.signal_engine import generate_signals

df_signals = generate_signals(filtered_df, pivots=pivots)

# Calcul des bornes de la session asiatique (0h–7h UTC)
df_asia = df_filtered_signals[df_filtered_signals["timestamp"].dt.hour.between(0, 6)]
asian_high = df_asia["high"].max()
asian_low = df_asia["low"].min()

# Optimisation des paramètres du moteur
if st.checkbox("🧪 Optimiser les paramètres du moteur"):
    param_grid = {
        "ema_period": [95, 114, 133],
        "cog_length": [14, 19, 38],
        "atr_mult": [1.5, 2.0, 2.5],
        "energy_threshold": [0.0, 0.2, 0.5]
    }
    df_results = optimize_parameters(df_filtered_signals, param_grid)
    st.dataframe(df_results.sort_values("Sharpe simplifié", ascending=False).head(10))
    df_results.to_csv("data/logs/optimization_results.csv", index=False)

# === Module export journal de trading + calcul de performance ===
from strategy.signal_engine import summarize_trades

trades, summary = summarize_trades(df_combined, pivots=pivots, asian_high=asian_high, asian_low=asian_low)
st.write("📘 Résumé des trades convergents :", summary)
trades.to_csv("data/logs/trade_journal.csv", index=False)
    
