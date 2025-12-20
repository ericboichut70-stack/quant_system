# modules/dashboard_refactor.py

import pandas as pd

def refactor_dashboard(df: pd.DataFrame) -> pd.DataFrame:
    """
    Réorganise le DataFrame du tableau de bord pour une meilleure lisibilité.
    
    Paramètres :
    - df : DataFrame contenant les métriques du bot
    
    Retour :
    - DataFrame restructuré avec colonnes normalisées et triées
    """
    df = df.copy()

    # Normalisation des noms de colonnes
    df.columns = [col.strip().capitalize() for col in df.columns]

    # Exemple de réorganisation : tri par capital décroissant
    if "Capital" in df.columns:
        df = df.sort_values("Capital", ascending=False)

    # Ajout d’une colonne de performance relative si Equity présent
    if "Equity" in df.columns and "Capital" in df.columns:
        df["PerformanceRatio"] = df["Equity"] / df["Capital"]

    return df


def summarize_dashboard(df: pd.DataFrame) -> str:
    """
    Génère un résumé textuel du tableau de bord.
    
    Paramètres :
    - df : DataFrame du tableau de bord
    
    Retour :
    - Chaîne descriptive avec métriques clés
    """
    if df.empty:
        return "📊 Tableau de bord vide."

    capital_avg = df["Capital"].mean() if "Capital" in df.columns else None
    equity_avg = df["Equity"].mean() if "Equity" in df.columns else None

    summary = "📊 Résumé du tableau de bord :\n"
    if capital_avg is not None:
        summary += f"- Capital moyen : {capital_avg:.2f}\n"
    if equity_avg is not None:
        summary += f"- Equity moyen : {equity_avg:.2f}\n"

    return summary
