import pandas as pd
from market_radar import compute_market_radar, summarize_market

# --- Création d’un DataFrame fictif ---
df_candles = pd.DataFrame([
    {"open": 100, "high": 105, "low": 95, "close": 102},
    {"open": 102, "high": 110, "low": 100, "close": 108},
    {"open": 108, "high": 109, "low": 95, "close": 96},
])

# --- Calcul du radar ---
radar = compute_market_radar(df_candles)
print("DataFrame enrichi :")
print(radar)

# --- Résumé global ---
summary = summarize_market(radar)
print("\nRésumé du radar :")
print(summary)
