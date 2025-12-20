import pandas as pd
from signal_predictor import extract_features, enrich_features, predict_signals

# --- Création d’un DataFrame fictif ---
df_prices = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","open":100,"high":105,"low":95,"close":100,"volume":800},
    {"timestamp":"2025-12-16 09:15:00","open":100,"high":106,"low":99,"close":102,"volume":1200},
    {"timestamp":"2025-12-16 09:30:00","open":102,"high":103,"low":95,"close":101,"volume":900},
    {"timestamp":"2025-12-16 09:45:00","open":101,"high":107,"low":100,"close":105,"volume":1500},
])

# --- Extraction des features ---
features = extract_features(df_prices)
print("Features extraits :")
print(features[["timestamp","Return","Volatility","VolumeNorm"]])

# --- Enrichissement ---
enriched = enrich_features(features)
print("\nFeatures enrichis :")
print(enriched[["timestamp","EMA","Momentum"]])

# --- Prédiction des signaux ---
predicted = predict_signals(enriched, threshold=0.01)
print("\nSignaux prédits :")
print(predicted[["timestamp","PredictedSignal"]])
