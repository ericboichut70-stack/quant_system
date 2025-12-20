# modules/multi_timeframe_convergence.py

import pandas as pd

def detect_convergence(df: pd.DataFrame, tf1: str="15T", tf2: str="1H") -> str:
    """
    Détecte convergence ou divergence entre deux timeframes.
    
    Paramètres :
    - df : DataFrame OHLC
    - tf1, tf2 : unités de temps
    
    Retour :
    - Chaîne descriptive
    """
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.set_index("timestamp")

    tf1_df = df.resample(tf1).agg({"open":"first","high":"max","low":"min","close":"last"}).dropna()
    tf2_df = df.resample(tf2).agg({"open":"first","high":"max","low":"min","close":"last"}).dropna()

    trend1 = "Bullish" if tf1_df.iloc[-1]["close"]>tf1_df.iloc[-2]["close"] else "Bearish"
    trend2 = "Bullish" if tf2_df.iloc[-1]["close"]>tf2_df.iloc[-2]["close"] else "Bearish"

    return "📊 Convergence : tendances alignées." if trend1==trend2 else f"⚠️ Divergence : {trend1} vs {trend2}"
