# modules/fvg_detector.py

import pandas as pd

def detect_fvg(df: pd.DataFrame) -> pd.DataFrame:
    """
    Détecte les Fair Value Gaps (FVG) dans une série de bougies.
    
    Paramètres :
    - df : DataFrame contenant au minimum ['open', 'high', 'low', 'close']
    
    Retour :
    - DataFrame enrichi avec une colonne 'FVG' :
      * 'Bullish' si FVG haussier détecté
      * 'Bearish' si FVG baissier détecté
      * None sinon
    """
    df = df.copy()
    df["FVG"] = None

    # Parcours des bougies avec fenêtre de 3
    for i in range(2, len(df)):
        low3 = df.at[i, "low"]
        high3 = df.at[i, "high"]
        low1 = df.at[i-2, "low"]
        high1 = df.at[i-2, "high"]

        # FVG haussier : low de bougie 3 > high de bougie 1
        if low3 > high1:
            df.at[i, "FVG"] = "Bullish"

        # FVG baissier : high de bougie 3 < low de bougie 1
        elif high3 < low1:
            df.at[i, "FVG"] = "Bearish"

    return df
