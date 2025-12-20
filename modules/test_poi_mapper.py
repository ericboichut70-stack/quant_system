import pandas as pd
from poi_mapper import detect_poi, summarize_poi

# --- Création d’un DataFrame fictif ---
df_candles = pd.DataFrame([
    {"open":100,"high":105,"low":95,"close":102},
    {"open":102,"high":108,"low":100,"close":107},
    {"open":107,"high":110,"low":105,"close":109},  # résistance locale
    {"open":109,"high":111,"low":108,"close":110},
    {"open":110,"high":112,"low":109,"close":111},  # support local
])

# --- Détection ---
result = detect_poi(df_candles, window=1)
print(result[["open","high","low","close","POI"]])

# --- Résumé ---
print(summarize_poi(result))
