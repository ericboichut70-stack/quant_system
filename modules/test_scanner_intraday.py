import pandas as pd
from scanner_intraday import compute_intraday_trend, correlate_with_bot_signals, filter_intraday

# --- Création d’un DataFrame fictif ---
df_candles = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","close":100,"NewsImpact":False,"TooDirectional":False},
    {"timestamp":"2025-12-16 09:15:00","close":102,"NewsImpact":False,"TooDirectional":False},
    {"timestamp":"2025-12-16 09:30:00","close":101,"NewsImpact":True,"TooDirectional":False},   # filtrée
    {"timestamp":"2025-12-16 09:45:00","close":105,"NewsImpact":False,"TooDirectional":True},   # filtrée
])

# --- Calcul de tendance ---
df_candles["Trend"] = compute_intraday_trend(df_candles)

# --- Corrélation avec signaux du bot ---
bot_signals = pd.Series({"2025-12-16 09:00:00":"Bullish","2025-12-16 09:15:00":"Bullish"})
df_candles["AlignedWithBot"] = correlate_with_bot_signals(df_candles, bot_signals)

# --- Filtrage ---
filtered = filter_intraday(df_candles)

print("DataFrame enrichi :")
print(df_candles)

print("\nDataFrame filtré :")
print(filtered)
