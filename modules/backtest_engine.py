import pandas as pd
import numpy as np

def run_backtest(df: pd.DataFrame) -> pd.DataFrame:
    """
    Exécute un backtest simplifié sur les signaux convergents.
    
    Paramètres :
    - df : DataFrame contenant au minimum ['timestamp', 'close', 'StopLoss', 'TakeProfit', 'PositionSize', 'BuyCombined', 'SellCombined', 'TrendCode']
    
    Retour :
    - DataFrame journalisant chaque trade exécuté avec direction, entrée, sortie, PnL et equity.
    """
    df = df.copy()
    trades = []

    capital = 100000
    equity = capital

    for i, row in df.iterrows():
        if not row.get("BuyCombined") and not row.get("SellCombined"):
            continue

        entry_price = row["close"]
        sl = row.get("StopLoss")
        tp = row.get("TakeProfit")
        size = row.get("PositionSize", 0)
        direction = "Buy" if row.get("BuyCombined") else "Sell"

        if pd.isna(sl) or pd.isna(tp) or size == 0:
            continue

        # Règle de simulation :
        # - Si TrendCode correspond à la direction du trade → TP atteint
        # - Sinon → SL atteint
        simulated_outcome = "TP" if row.get("TrendCode", 0) == (1 if direction == "Buy" else -1) else "SL"
        exit_price = tp if simulated_outcome == "TP" else sl
        pnl = (exit_price - entry_price) * size if direction == "Buy" else (entry_price - exit_price) * size
        equity += pnl

        trades.append({
            "timestamp": row["timestamp"],
            "Direction": direction,
            "Entry": entry_price,
            "Exit": exit_price,
            "Size": size,
            "PnL": pnl,
            "Equity": equity,
            "Outcome": simulated_outcome
        })

    return pd.DataFrame(trades)
