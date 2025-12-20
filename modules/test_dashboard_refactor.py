import pandas as pd
from dashboard_refactor import refactor_dashboard, summarize_dashboard

# --- Création d’un DataFrame fictif ---
df = pd.DataFrame([
    {"Capital": 100000, "Equity": 105000},
    {"Capital": 80000, "Equity": 79000},
    {"Capital": 120000, "Equity": 130000},
])

# --- Test refactorisation ---
refactored = refactor_dashboard(df)
print("DataFrame refactorisé :")
print(refactored)

# --- Test résumé ---
summary = summarize_dashboard(refactored)
print("\nRésumé généré :")
print(summary)
