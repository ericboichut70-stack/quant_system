# modules/market_radar.py

import pandas as pd

def compute_market_radar(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcule des indicateurs simples de marché pour chaque bougie.
    
    Paramètres :
    - df : DataFrame contenant au minimum ['open', 'high', 'low', 'close']
    
    Retour :
    - DataFrame enrichi avec colonnes :
      * 'Range' : amplitude de la bougie (high - low)
      * 'Direction' : 'Bullish' si close > open, 'Bearish' sinon
      * 'Volatility' : ratio range / close
    """
    df = df.copy()
    df["Range"] = df["high"] - df["low"]
    df["Direction"] = df.apply(lambda r: "Bullish" if r["close"] > r["open"] else "Bearish", axis=1)
    df["Volatility"] = df["Range"] / df["close"]
    return df


def summarize_market(df: pd.DataFrame) -> str:
    """
    Génère un résumé global des conditions de marché.
    
    Paramètres :
    - df : DataFrame enrichi par compute_market_radar
    
    Retour :
    - Chaîne descriptive avec volatilité moyenne et proportion de bougies haussières
    """
    if df.empty:
        return "📊 Aucun signal de marché disponible."

    vol_avg = df["Volatility"].mean()
    bullish_ratio = (df["Direction"] == "Bullish").mean() * 100

    summary = "📊 Radar de marché :\n"
    summary += f"- Volatilité moyenne : {vol_avg:.4f}\n"
    summary += f"- Bougies haussières : {bullish_ratio:.2f}%\n"
    return summary
