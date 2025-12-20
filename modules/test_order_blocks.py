import pandas as pd
from order_blocks import detect_order_blocks, summarize_order_blocks

# --- Création d’un DataFrame fictif ---
df_candles = pd.DataFrame([
    {"open": 100, "high": 105, "low": 95, "close": 100},
    {"open": 100, "high": 106, "low": 99, "close": 102},   # +2% → Bullish OB
    {"open": 102, "high": 103, "low": 95, "close": 97},    # -5% → Bearish OB
    {"open": 97,  "high": 98,  "low": 96, "close": 97},    # pas de rupture
])

# --- Détection ---
result = detect_order_blocks(df_candles)
print(result[["open","high","low","close","OrderBlock"]])

# --- Résumé ---
print(summarize_order_blocks(result))
