import pandas as pd
from propfirm_compatibility_checker import check_propfirm_rules, summarize_rules

# --- Création d’un DataFrame fictif de trades ---
df_trades = pd.DataFrame([
    {"timestamp":"2025-12-16 10:00:00","PnL":100,"Equity":100100,"Risk":500},
    {"timestamp":"2025-12-16 11:00:00","PnL":50,"Equity":100150,"Risk":400},
    {"timestamp":"2025-12-16 12:00:00","PnL":-80,"Equity":100070,"Risk":600},
])

# --- Création d’un DataFrame de règles ---
df_rules = pd.DataFrame([
    {"Rule":"MaxDrawdown","Value":-1000},
    {"Rule":"MaxRiskPerTrade","Value":1000},
    {"Rule":"MinTradingDays","Value":2},
])

# --- Vérification ---
results = check_propfirm_rules(df_trades, df_rules)
print("Résultats détaillés :")
print(results)

# --- Résumé ---
print("\nRésumé :")
print(summarize_rules(results))
