import pandas as pd
from account_router import route_signals_to_accounts

# --- Création d'un DataFrame de signaux ---
df_signals = pd.DataFrame([
    {"timestamp": "2025-12-16 15:00:00", "Duration": 30},   # signal daytime, intraday
    {"timestamp": "2025-12-16 23:00:00", "Duration": 120},  # signal overnight, swing
])

# --- Création d'un DataFrame de comptes ---
accounts_df = pd.DataFrame([
    {"name": "Compte_A", "news_allowed": True, "overnight_allowed": False, "type": "intraday", "max_drawdown": 5000},
    {"name": "Compte_B", "news_allowed": True, "overnight_allowed": True,  "type": "swing",    "max_drawdown": 15000},
    {"name": "Compte_C", "news_allowed": True, "overnight_allowed": True,  "type": "intraday", "max_drawdown": 10000},
])

# --- Exécution de la fonction ---
result = route_signals_to_accounts(df_signals, accounts_df)

# --- Affichage du résultat ---
print(result)
