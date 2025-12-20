# modules/poi_mapper.py

import pandas as pd

def detect_poi(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    """
    Détecte des points d’intérêt (POI) dans une série de bougies.
    
    Paramètres :
    - df : DataFrame contenant ['open','high','low','close']
    - window : nombre de bougies pour comparer (par défaut 3)
    
    Retour :
    - DataFrame enrichi avec colonne 'POI' :
      * 'Support' si low[i] est inférieur aux lows voisins
      * 'Resistance' si high[i] est supérieur aux highs voisins
      * None sinon
    """
    df = df.copy()
    df["POI"] = None

    for i in range(window, len(df) - window):
        local_low = df["low"].iloc[i-window:i+window+1].min()
        local_high = df["high"].iloc[i-window:i+window+1].max()

        if df.at[i, "low"] == local_low:
            df.at[i, "POI"] = "Support"
        elif df.at[i, "high"] == local_high:
            df.at[i, "POI"] = "Resistance"

    return df


def summarize_poi(df: pd.DataFrame) -> str:
    """
    Résume les points d’intérêt détectés.
    """
    if df.empty:
        return "📊 Aucun POI détecté."

    support_count = (df["POI"] == "Support").sum()
    resistance_count = (df["POI"] == "Resistance").sum()

    return f"📊 Points d’intérêt : Supports={support_count}, Résistances={resistance_count}"
