import pandas as pd
from sentiment_analyzer import analyze_sentiment, summarize_sentiment

# --- Création d’un DataFrame fictif ---
df_prices = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","close":100},
    {"timestamp":"2025-12-16 09:15:00","close":102},  # Positive
    {"timestamp":"2025-12-16 09:30:00","close":101},  # Negative
    {"timestamp":"2025-12-16 09:45:00","close":101},  # Neutral
])

# --- Analyse du sentiment ---
result = analyze_sentiment(df_prices)
print("DataFrame enrichi :")
print(result)

# --- Résumé ---
summary = summarize_sentiment(result)
print("\nRésumé :")
print(summary)
