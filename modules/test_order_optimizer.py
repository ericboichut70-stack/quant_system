import pandas as pd
from order_optimizer import optimize_signals, summarize_optimization

# --- Création d’un DataFrame fictif ---
df_signals = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","Energy":0.6,"RiskReward":2.0,"TrendCode":1},
    {"timestamp":"2025-12-16 09:15:00","Energy":0.4,"RiskReward":1.8,"TrendCode":1},  # filtré (Energy trop faible)
    {"timestamp":"2025-12-16 09:30:00","Energy":0.7,"RiskReward":1.2,"TrendCode":0},  # pas convergent
])

params = {"min_energy":0.5,"rr_threshold":1.5}

# --- Optimisation ---
optimized = optimize_signals(df_signals, params)
print("DataFrame optimisé :")
print(optimized)

# --- Résumé ---
summary = summarize_optimization(optimized)
print("\nRésumé :")
print(summary)
