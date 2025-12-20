# modules/trend_detector.py

import pandas as pd

def compute_ema_slope(df: pd.DataFrame, period: int = 10) -> pd.Series:
    """
    Calcule la pente de l'EMA pour détecter la direction de la tendance.

    Paramètres :
    - df : DataFrame contenant ['close']
    - period : période de l'EMA

    Retour :
    - Série contenant la pente (différence EMA_t - EMA_{t-1})
    """
    ema = df["close"].ewm(span=period).mean()
    slope = ema.diff().fillna(0)
    return slope


def compute_adx_simplified(df: pd.DataFrame, period: int = 14) -> pd.Series:
    """
    Calcule un ADX simplifié basé sur la variation moyenne du True Range.

    Paramètres :
    - df : DataFrame contenant ['high','low','close']
    - period : période de lissage

    Retour :
    - Série représentant un ADX simplifié (0 à ~1)
    """
    tr = (df["high"] - df["low"]).abs()
    adx = tr.rolling(period).mean().fillna(0)
    adx_norm = adx / adx.max() if adx.max() != 0 else adx
    return adx_norm


def detect_trend(df: pd.DataFrame, slope_threshold: float = 0.05, adx_threshold: float = 0.3) -> pd.DataFrame:
    """
    Détecte la tendance du marché en combinant :
    - la pente de l'EMA
    - un ADX simplifié

    Paramètres :
    - df : DataFrame contenant ['timestamp','high','low','close']
    - slope_threshold : seuil pour considérer la pente comme significative
    - adx_threshold : seuil pour considérer la tendance comme forte

    Retour :
    - DataFrame enrichi avec :
      * 'Slope'
      * 'ADX'
      * 'Trend' : 'Bullish', 'Bearish', 'Range'
      * 'TrendCode' : 1 (bull), -1 (bear), 0 (range)
    """
    df = df.copy()

    df["Slope"] = compute_ema_slope(df)
    df["ADX"] = compute_adx_simplified(df)

    df["Trend"] = "Range"
    df["TrendCode"] = 0

    for i, row in df.iterrows():
        slope = row["Slope"]
        adx = row["ADX"]

        if adx < adx_threshold:
            df.at[i, "Trend"] = "Range"
            df.at[i, "TrendCode"] = 0
            continue

        if slope > slope_threshold:
            df.at[i, "Trend"] = "Bullish"
            df.at[i, "TrendCode"] = 1

        elif slope < -slope_threshold:
            df.at[i, "Trend"] = "Bearish"
            df.at[i, "TrendCode"] = -1

        else:
            df.at[i, "Trend"] = "Range"
            df.at[i, "TrendCode"] = 0

    return df
