import pandas as pd
from backtest_engine import run_backtest

# --- Création d’un DataFrame fictif de signaux ---
df_signals = pd.DataFrame([
    {
        "timestamp": "2025-12-16 10:00:00",
        "close": 100,
        "StopLoss": 95,
        "TakeProfit": 110,
        "PositionSize": 10,
        "BuyCombined": True,
        "SellCombined": False,
        "TrendCode": 1,   # tendance haussière
    },
    {
        "timestamp": "2025-12-16 11:00:00",
        "close": 200,
        "StopLoss": 210,
        "TakeProfit": 190,
        "PositionSize": 5,
        "BuyCombined": False,
        "SellCombined": True,
        "TrendCode": -1,  # tendance baissière
    },
    {
        "timestamp": "2025-12-16 12:00:00",
        "close": 150,
        "StopLoss": 140,
        "TakeProfit": 160,
        "PositionSize": 8,
        "BuyCombined": True,
        "SellCombined": False,
        "TrendCode": -1,  # tendance contraire
    },
])

# --- Exécution du backtest ---
result = run_backtest(df_signals)

# --- Affichage du journal des trades ---
print(result)
