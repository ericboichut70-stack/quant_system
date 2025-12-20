# modules/performance_dashboard.py

import pandas as pd

def build_performance_dashboard(df: pd.DataFrame) -> pd.DataFrame:
    """
    Construit un tableau de bord de performance à partir des trades.
    
    Paramètres :
    - df : DataFrame contenant ['timestamp','Direction','Entry','Exit','Size','PnL','Outcome']
    
    Retour :
    - DataFrame avec colonnes de performance agrégée :
      * 'TotalPnL'
      * 'WinRate'
      * 'AveragePnL'
      * 'MaxDrawdown'
    """
    if df.empty:
        return pd.DataFrame([{
            "TotalPnL": 0,
            "WinRate": 0,
            "AveragePnL": 0,
            "MaxDrawdown": 0
        }])

    total_pnl = df["PnL"].sum()
    win_rate = (df["Outcome"] == "TP").mean() * 100
    avg_pnl = df["PnL"].mean()

    # Calcul du drawdown maximum
    equity_curve = df["PnL"].cumsum()
    rolling_max = equity_curve.cummax()
    drawdowns = equity_curve - rolling_max
    max_drawdown = drawdowns.min()

    dashboard = pd.DataFrame([{
        "TotalPnL": total_pnl,
        "WinRate": win_rate,
        "AveragePnL": avg_pnl,
        "MaxDrawdown": max_drawdown
    }])

    return dashboard


def summarize_dashboard(dashboard: pd.DataFrame) -> str:
    """
    Génère un résumé textuel du tableau de bord de performance.
    """
    if dashboard.empty:
        return "📊 Aucun résultat de performance."

    row = dashboard.iloc[0]
    summary = "📊 Performance Dashboard :\n"
    summary += f"- PnL total : {row['TotalPnL']:.2f}\n"
    summary += f"- Taux de réussite : {row['WinRate']:.2f}%\n"
    summary += f"- PnL moyen : {row['AveragePnL']:.2f}\n"
    summary += f"- Max Drawdown : {row['MaxDrawdown']:.2f}\n"
    return summary
