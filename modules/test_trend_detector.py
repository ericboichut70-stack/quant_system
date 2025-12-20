import pandas as pd
from trend_detector import detect_trend

# --- Données fictives ---
df_prices = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","high":100,"low":95,"close":98},
    {"timestamp":"2025-12-16 09:15:00","high":102,"low":97,"close":101},
    {"timestamp":"2025-12-16 09:30:00","high":105,"low":100,"close":104},
    {"timestamp":"2025-12-16 09:45:00","high":107,"low":103,"close":106},
    {"timestamp":"2025-12-16 10:00:00","high":108,"low":104,"close":107},
])

# --- Détection de tendance ---
trend = detect_trend(df_prices, slope_threshold=0.02, adx_threshold=0.1)

print("DataFrame enrichi :")
print(trend)

print("\nRésumé des tendances :")
print(trend[["timestamp","Trend","TrendCode"]])
