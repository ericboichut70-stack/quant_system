import pandas as pd
from scenario_builder import build_scenarios, summarize_scenarios

# --- Création d’un DataFrame fictif ---
df_signals = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","Trend":"Bullish","Signal":"Buy","RiskReward":2.0},
    {"timestamp":"2025-12-16 09:15:00","Trend":"Bearish","Signal":"Sell","RiskReward":1.5},
    {"timestamp":"2025-12-16 09:30:00","Trend":"Bullish","Signal":"Sell","RiskReward":1.2},
    {"timestamp":"2025-12-16 09:45:00","Trend":"Neutral","Signal":"Buy","RiskReward":1.0},
])

# --- Construction des scénarios ---
scenarios = build_scenarios(df_signals)
print("DataFrame enrichi :")
print(scenarios)

# --- Résumé ---
summary = summarize_scenarios(scenarios)
print("\nRésumé :")
print(summary)
