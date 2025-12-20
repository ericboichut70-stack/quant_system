import pandas as pd
from volatility_clustering import compute_volatility, detect_volatility_clusters

# --- Données fictives ---
df_prices = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","close":100},
    {"timestamp":"2025-12-16 09:15:00","close":102},
    {"timestamp":"2025-12-16 09:30:00","close":101},
    {"timestamp":"2025-12-16 09:45:00","close":105},
    {"timestamp":"2025-12-16 10:00:00","close":103},
    {"timestamp":"2025-12-16 10:15:00","close":110},
])

# --- Calcul de volatilité ---
vol = compute_volatility(df_prices)
print("Volatilité :")
print(vol)

# --- Détection des clusters ---
clusters = detect_volatility_clusters(df_prices, threshold=0.015)
print("\nClusters détectés :")
print(clusters)
