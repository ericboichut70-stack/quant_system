import pandas as pd
from zigzag_mapper import compute_zigzag, summarize_zigzag

# --- Données fictives ---
df_prices = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","close":100},
    {"timestamp":"2025-12-16 09:15:00","close":104},  # +4% → High
    {"timestamp":"2025-12-16 09:30:00","close":102},
    {"timestamp":"2025-12-16 09:45:00","close":96},   # -7.7% → Low
    {"timestamp":"2025-12-16 10:00:00","close":99},
    {"timestamp":"2025-12-16 10:15:00","close":103},  # +4% → High
])

# --- Calcul ZigZag ---
zigzag = compute_zigzag(df_prices, threshold=0.02)
print("DataFrame enrichi :")
print(zigzag)

# --- Résumé ---
summary = summarize_zigzag(zigzag)
print("\nRésumé :")
print(summary)
