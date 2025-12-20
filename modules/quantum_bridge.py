# modules/quantum_bridge.py

import pandas as pd

def build_quantum_bridge(signals_list: list) -> pd.DataFrame:
    """
    Construit une passerelle (bridge) entre plusieurs ensembles de signaux.
    
    Paramètres :
    - signals_list : liste de DataFrames contenant chacun des signaux
      (avec colonnes ['timestamp','Signal','Strength'])
    
    Retour :
    - DataFrame consolidé avec colonnes :
      * 'timestamp'
      * 'Signal'
      * 'Strength'
      * 'Source' (nom ou index du flux d’origine)
    """
    consolidated = []
    for idx, df in enumerate(signals_list):
        for _, row in df.iterrows():
            consolidated.append({
                "timestamp": row["timestamp"],
                "Signal": row["Signal"],
                "Strength": row["Strength"],
                "Source": f"Stream_{idx+1}"
            })
    return pd.DataFrame(consolidated)


def summarize_bridge(df: pd.DataFrame) -> str:
    """
    Génère un résumé de cohérence du quantum bridge.
    
    Paramètres :
    - df : DataFrame consolidé
    
    Retour :
    - Chaîne descriptive indiquant nombre de flux, signaux et moyenne de force
    """
    if df.empty:
        return "🌌 Quantum Bridge : aucun signal consolidé."

    sources = df["Source"].nunique()
    total_signals = len(df)
    avg_strength = df["Strength"].mean()

    summary = "🌌 Quantum Bridge Résumé :\n"
    summary += f"- Flux connectés : {sources}\n"
    summary += f"- Nombre total de signaux : {total_signals}\n"
    summary += f"- Force moyenne : {avg_strength:.2f}\n"
    return summary
