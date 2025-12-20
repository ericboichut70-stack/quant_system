# modules/propfirm_compatibility_checker.py

import pandas as pd

def check_propfirm_rules(trades: pd.DataFrame, rules_df: pd.DataFrame) -> pd.DataFrame:
    """
    Vérifie la compatibilité des trades avec les règles d'une prop firm.
    
    Paramètres :
    - trades : DataFrame contenant ['timestamp','PnL','Equity','Risk']
    - rules_df : DataFrame contenant les règles (ex. {'Rule':'MaxDrawdown','Value':-5000})
    
    Retour :
    - DataFrame enrichi avec colonne 'RuleCheck' indiquant True/False pour chaque règle
    """
    results = []

    for _, rule in rules_df.iterrows():
        rule_name = rule["Rule"]
        value = rule["Value"]

        if rule_name == "MaxDrawdown":
            equity_curve = trades["PnL"].cumsum()
            rolling_max = equity_curve.cummax()
            drawdowns = equity_curve - rolling_max
            max_dd = drawdowns.min()
            results.append({"Rule": rule_name, "Value": value, "RuleCheck": max_dd >= value})

        elif rule_name == "MaxRiskPerTrade":
            max_risk = trades["Risk"].max()
            results.append({"Rule": rule_name, "Value": value, "RuleCheck": max_risk <= value})

        elif rule_name == "MinTradingDays":
            unique_days = trades["timestamp"].apply(lambda x: str(x).split(" ")[0]).nunique()
            results.append({"Rule": rule_name, "Value": value, "RuleCheck": unique_days >= value})

        else:
            results.append({"Rule": rule_name, "Value": value, "RuleCheck": None})

    return pd.DataFrame(results)


def summarize_rules(results: pd.DataFrame) -> str:
    """
    Génère un résumé textuel de la compatibilité avec les règles.
    """
    if results.empty:
        return "📊 Aucune règle vérifiée."

    summary = "📊 Résultats de compatibilité prop firm :\n"
    for _, row in results.iterrows():
        status = "✅ Respectée" if row["RuleCheck"] else "❌ Non respectée"
        summary += f"- {row['Rule']} (valeur={row['Value']}) : {status}\n"
    return summary
