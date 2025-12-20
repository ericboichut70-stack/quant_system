# modules/mitigation_mapper.py

import pandas as pd

def detect_mitigation_zones(df: pd.DataFrame) -> pd.DataFrame:
    """
    Détecte les zones de mitigation dans une série de bougies.
    
    Paramètres :
    - df : DataFrame contenant ['open', 'high', 'low', 'close']
    
    Retour :
    - DataFrame enrichi avec colonne 'MitigationZone' :
      * 'Bullish' si la bougie actuelle revient combler un gap haussier
      * 'Bearish' si la bougie actuelle revient combler un gap baissier
      * None sinon
    """
    df = df.copy()
    df["MitigationZone"] = None

    for i in range(2, len(df)):
        # Détection d’un gap haussier : low[i] > high[i-2]
        if df.at[i, "low"] > df.at[i-2, "high"]:
            df.at[i, "MitigationZone"] = "Bullish"

        # Détection d’un gap baissier : high[i] < low[i-2]
        elif df.at[i, "high"] < df.at[i-2, "low"]:
            df.at[i, "MitigationZone"] = "Bearish"

    return df


def summarize_mitigation(df: pd.DataFrame) -> str:
    """
    Résume les zones de mitigation détectées.
    """
    if df.empty:
        return "📊 Aucune zone de mitigation détectée."

    bullish_count = (df["MitigationZone"] == "Bullish").sum()
    bearish_count = (df["MitigationZone"] == "Bearish").sum()

    return f"📊 Zones de mitigation : Haussières={bullish_count}, Baissières={bearish_count}"
