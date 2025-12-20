import pandas as pd
from signal_attribution import attribute_signals, summarize_attribution

# --- Création d’un DataFrame fictif ---
df_signals = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","Signal":"Buy","Trend":"Buy","Volume":800,"Sentiment":"Neutral"},   # Trend
    {"timestamp":"2025-12-16 09:15:00","Signal":"Sell","Trend":"Buy","Volume":1500,"Sentiment":"Neutral"}, # Volume
    {"timestamp":"2025-12-16 09:30:00","Signal":"Buy","Trend":"Sell","Volume":500,"Sentiment":"Positive"}, # Sentiment
    {"timestamp":"2025-12-16 09:45:00","Signal":"Sell","Trend":"Sell","Volume":2000,"Sentiment":"Negative"}, # Mixed
    {"timestamp":"2025-12-16 10:00:00","Signal":"Buy","Trend":"Neutral","Volume":300,"Sentiment":"Neutral"}, # Unclear
])

# --- Attribution ---
result = attribute_signals(df_signals)
print("DataFrame enrichi :")
print(result)

# --- Résumé ---
summary = summarize_attribution(result)
print("\nRésumé :")
print(summary)
