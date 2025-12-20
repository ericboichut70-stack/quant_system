# modules/order_blocks.py

import pandas as pd

def detect_order_blocks(df: pd.DataFrame, threshold: float = 0.01) -> pd.DataFrame:
    """
    Détecte des ruptures de prix assimilées à des order blocks.
    
    Paramètres :
    - df : DataFrame contenant ['open','high','low','close']
    - threshold : pourcentage de variation (par défaut 1%)
    
    Retour :
    - DataFrame enrichi avec colonne 'OrderBlock' :
      * 'Bullish' si close > prev_close * (1+threshold)
      * 'Bearish' si close < prev_close * (1-threshold)
      * None sinon
    """
    df = df.copy()
    df["OrderBlock"] = None

    for i in range(1, len(df)):
        prev_close = df.at[i-1, "close"]
        curr_close = df.at[i, "close"]

        if curr_close > prev_close * (1 + threshold):
            df.at[i, "OrderBlock"] = "Bullish"
        elif curr_close < prev_close * (1 - threshold):
            df.at[i, "OrderBlock"] = "Bearish"

    return df


def summarize_order_blocks(df: pd.DataFrame) -> str:
    """
    Résume les order blocks détectés.
    """
    if df.empty:
        return "📊 Aucun order block détecté."

    bullish_count = (df["OrderBlock"] == "Bullish").sum()
    bearish_count = (df["OrderBlock"] == "Bearish").sum()

    return f"📊 Order Blocks : Haussiers={bullish_count}, Baissiers={bearish_count}"
