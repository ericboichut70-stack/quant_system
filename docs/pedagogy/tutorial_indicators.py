
# === Imports et configuration du chemin ===
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

import pandas as pd
import numpy as np
from indicators.base_indicators import IndicatorModule

# === Fonction de génération de données simulées ===
import yfinance as yf

df = yf.download("AAPL", start="2022-01-01", end="2023-01-01", interval="1d")
df = df.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'})

# === Initialisation du module ===
indicator = IndicatorModule(ema_period=20, rsi_period=14, volume_ratio_thresh=1.5)

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

    indicator = IndicatorModule(ema, rsi, volume_thresh)
    df_ind = indicator.compute_indicators(df)
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

df_trades.to_csv("signaux_trading.csv")
