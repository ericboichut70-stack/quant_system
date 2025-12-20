# modules/multi_tf_contextualizer.py

import pandas as pd

def add_timeframe_context(df: pd.DataFrame, higher_tf: str = "1H") -> pd.DataFrame:
    """
    Enrichit les signaux avec le contexte d’un timeframe supérieur.
    
    Paramètres :
    - df : DataFrame avec ['timestamp','open','high','low','close']
    - higher_tf : unité de temps supérieure (ex. '1H','1D')
    
    Retour :
    - DataFrame enrichi avec colonne 'HigherTFTrend'
    """
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.set_index("timestamp")

    higher = df.resample(higher_tf).agg({"open":"first","high":"max","low":"min","close":"last"}).dropna()
    higher["Trend"] = higher["close"].diff().apply(lambda x: "Bullish" if x>0 else "Bearish")

    # Mapping du contexte sur les signaux
    df = df.reset_index()
    df["HigherTFTrend"] = None
    for i,row in df.iterrows():
        ts = row["timestamp"]
        # trouver la bougie higher_tf correspondante
        ht = higher.loc[higher.index.floor(higher_tf)==ts.floor(higher_tf)]
        if not ht.empty:
            df.at[i,"HigherTFTrend"] = ht.iloc[-1]["Trend"]

    return df
