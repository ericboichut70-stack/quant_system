import pandas as pd
from explainable_ai import explain_trade_decision, explain_backtest_results

# --- Création d’un DataFrame fictif de trades ---
df_trades = pd.DataFrame([
    {"timestamp": "2025-12-16 10:00:00", "Direction": "Buy",  "Entry": 100, "Exit": 110, "Size": 10, "PnL": 100, "Equity": 100100, "Outcome": "TP"},
    {"timestamp": "2025-12-16 11:00:00", "Direction": "Sell", "Entry": 200, "Exit": 190, "Size": 5,  "PnL": 50,  "Equity": 100150, "Outcome": "TP"},
    {"timestamp": "2025-12-16 12:00:00", "Direction": "Buy",  "Entry": 150, "Exit": 140, "Size": 8,  "PnL": -80, "Equity": 100070, "Outcome": "SL"},
])

# --- Test explication individuelle ---
print("Explication d’un trade :")
print(explain_trade_decision(df_trades.iloc[0]))

# --- Test résumé global ---
print("\nRésumé du backtest :")
print(explain_backtest_results(df_trades))
