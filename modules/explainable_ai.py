# modules/explainable_ai.py

import pandas as pd

def explain_trade_decision(trade_row: pd.Series) -> str:
    """
    Génère une explication pédagogique pour une décision de trade.
    
    Paramètres :
    - trade_row : ligne d'un DataFrame contenant au minimum
      ['timestamp', 'Direction', 'Entry', 'Exit', 'Size', 'PnL', 'Outcome']
    
    Retour :
    - Chaîne descriptive expliquant la logique du trade
    """
    ts = trade_row.get("timestamp", "N/A")
    direction = trade_row.get("Direction", "N/A")
    entry = trade_row.get("Entry", None)
    exit_price = trade_row.get("Exit", None)
    pnl = trade_row.get("PnL", 0)
    outcome = trade_row.get("Outcome", "N/A")

    explanation = f"📈 Trade du {ts} :\n"
    explanation += f"- Direction : {direction}\n"
    explanation += f"- Entrée à {entry}, sortie à {exit_price}\n"
    explanation += f"- Résultat : {outcome} avec PnL = {pnl}\n"

    if outcome == "TP":
        explanation += "✅ Le Take Profit a été atteint grâce à une tendance favorable.\n"
    elif outcome == "SL":
        explanation += "❌ Le Stop Loss a été déclenché car la tendance était contraire.\n"
    else:
        explanation += "ℹ️ Issue indéterminée.\n"

    return explanation


def explain_backtest_results(df_trades: pd.DataFrame) -> str:
    """
    Fournit un résumé pédagogique des résultats d’un backtest.
    
    Paramètres :
    - df_trades : DataFrame des trades exécutés
    
    Retour :
    - Chaîne descriptive avec nombre de trades, taux de réussite et PnL total
    """
    if df_trades.empty:
        return "📊 Aucun trade exécuté."

    total_trades = len(df_trades)
    tp_count = (df_trades["Outcome"] == "TP").sum()
    sl_count = (df_trades["Outcome"] == "SL").sum()
    pnl_total = df_trades["PnL"].sum()

    success_rate = tp_count / total_trades * 100

    summary = "📊 Résultats du backtest :\n"
    summary += f"- Nombre total de trades : {total_trades}\n"
    summary += f"- Take Profit : {tp_count}, Stop Loss : {sl_count}\n"
    summary += f"- Taux de réussite : {success_rate:.2f}%\n"
    summary += f"- PnL total : {pnl_total:.2f}\n"

    return summary
