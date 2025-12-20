# modules/zigzag_mapper.py

import pandas as pd

def compute_zigzag(df: pd.DataFrame, threshold: float = 0.02) -> pd.DataFrame:
    """
    Calcule un ZigZag simplifié basé sur les variations relatives du prix.

    Paramètres :
    - df : DataFrame contenant ['timestamp','close']
    - threshold : variation minimale (en %) pour valider un pivot

    Retour :
    - DataFrame enrichi avec :
      * 'Pivot' : True/False
      * 'PivotType' : 'High' / 'Low' / ''
    """
    df = df.copy()
    df["Pivot"] = False
    df["PivotType"] = ""

    last_pivot_price = df.loc[0, "close"]
    last_pivot_type = None  # 'High' ou 'Low'

    for i in range(1, len(df)):
        price = df.loc[i, "close"]
        variation = (price - last_pivot_price) / last_pivot_price

        # Détection d'un pivot haut
        if variation > threshold and last_pivot_type != "High":
            df.at[i, "Pivot"] = True
            df.at[i, "PivotType"] = "High"
            last_pivot_price = price
            last_pivot_type = "High"

        # Détection d'un pivot bas
        elif variation < -threshold and last_pivot_type != "Low":
            df.at[i, "Pivot"] = True
            df.at[i, "PivotType"] = "Low"
            last_pivot_price = price
            last_pivot_type = "Low"

    return df


def summarize_zigzag(df: pd.DataFrame) -> str:
    """
    Résume les pivots ZigZag détectés.

    Paramètres :
    - df : DataFrame enrichi par compute_zigzag

    Retour :
    - Chaîne descriptive indiquant le nombre de pivots hauts et bas
    """
    if df.empty:
        return "📊 ZigZag : aucun pivot détecté."

    highs = (df["PivotType"] == "High").sum()
    lows = (df["PivotType"] == "Low").sum()

    return f"📊 ZigZag : High={highs}, Low={lows}"
