import pandas as pd
from structure_tracker import detect_market_structure, summarize_structure

# --- DataFrame fictif avec highs/lows structurés ---
df_prices = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","high":100,"low":95},
    {"timestamp":"2025-12-16 09:15:00","high":102,"low":96},
    {"timestamp":"2025-12-16 09:30:00","high":101,"low":97},
    {"timestamp":"2025-12-16 09:45:00","high":104,"low":98},
    {"timestamp":"2025-12-16 10:00:00","high":103,"low":99},
])

# --- Détection de structure ---
result = detect_market_structure(df_prices)
print("DataFrame enrichi :")
print(result)

# --- Résumé ---
summary = summarize_structure(result)
print("\nRésumé :")
print(summary)
