# modules/order_optimizer.py

import pandas as pd

def optimize_signals(df: pd.DataFrame, params: dict) -> pd.DataFrame:
    """
    Optimise les signaux de trading selon des paramètres donnés.
    
    Paramètres :
    - df : DataFrame contenant les signaux bruts
    - params : dictionnaire de paramètres (ex. {"min_energy":0.5,"rr_threshold":1.5})
    
    Retour :
    - DataFrame enrichi avec colonnes filtrées et signaux convergents
    """
    df = df.copy()

    # Injecter les paramètres dans le moteur
    min_energy = params.get("min_energy", 0.5)
    rr_threshold = params.get("rr_threshold", 1.5)

    # Filtrage énergie
    if "Energy" in df.columns:
        df = df[df["Energy"] >= min_energy]

    # Générer signaux convergents
    df["ConvergentSignal"] = (df.get("RiskReward", 0) >= rr_threshold) & (df.get("TrendCode", 0) != 0)

    return df


def summarize_optimization(df: pd.DataFrame) -> str:
    """
    Résume les résultats de l’optimisation des signaux.
    """
    if df.empty:
        return "📊 Aucun signal optimisé."

    total = len(df)
    convergent = df["ConvergentSignal"].sum()

    return f"📊 Optimisation : {convergent}/{total} signaux convergents ({convergent/total*100:.2f}%)."
