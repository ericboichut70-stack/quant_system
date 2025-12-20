import pandas as pd
from fvg_detector import detect_fvg

# --- Création d’un DataFrame fictif de bougies ---
df_candles = pd.DataFrame([
    {"open": 100, "high": 105, "low": 95, "close": 102},
    {"open": 103, "high": 108, "low": 100, "close": 107},
    {"open": 110, "high": 115, "low": 109, "close": 114},  # low3=109 > high1=105 → Bullish FVG
    {"open": 112, "high": 113, "low": 90,  "close": 92},   # high3=113 < low1=95 → Bearish FVG
    {"open": 95,  "high": 97,  "low": 93,  "close": 94},
])

# --- Détection des FVG ---
result = detect_fvg(df_candles)

# --- Affichage du résultat ---
print(result[["open", "high", "low", "close", "FVG"]])
