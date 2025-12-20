import pandas as pd
from account_selector import select_best_account

# --- Création d'un DataFrame de comptes fictifs ---
accounts_df = pd.DataFrame([
    {"name": "Compte_A", "type": "intraday", "overnight_allowed": False, "news_allowed": True, "constance_required": False, "max_drawdown": 5000},
    {"name": "Compte_B", "type": "swing",    "overnight_allowed": True,  "news_allowed": True, "constance_required": True,  "max_drawdown": 15000},
    {"name": "Compte_C", "type": "intraday", "overnight_allowed": True,  "news_allowed": True, "constance_required": False, "max_drawdown": 10000},
])

# --- Tests de sélection ---
print("Test intraday (sans overnight) :")
print(select_best_account(accounts_df, strategy="intraday", allow_overnight=False))

print("\nTest intraday (avec overnight autorisé) :")
print(select_best_account(accounts_df, strategy="intraday", allow_overnight=True))

print("\nTest swing (overnight autorisé) :")
print(select_best_account(accounts_df, strategy="swing", allow_overnight=True))

print("\nTest overnight (avec constance requise) :")
print(select_best_account(accounts_df, strategy="overnight", allow_overnight=True, require_constance=True))
