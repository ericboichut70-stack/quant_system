# modules/scanner_intraday.py

import pandas as pd

def compute_intraday_trend(df: pd.DataFrame, period: int = 5) -> pd.Series:
    """
    Calcule une tendance intraday simple basée sur la pente de l'EMA.
    
    Paramètres :
    - df : DataFrame contenant ['close']
    - period : période de l'EMA (par défaut 5)
    
    Retour :
    - Série indiquant 'Bullish', 'Bearish' ou 'Neutral' pour chaque bougie
    """
    ema = df["close"].ewm(span=period).mean()
    slope = ema.diff()
    trend = slope.apply(lambda x: "Bullish" if x > 0 else ("Bearish" if x < 0 else "Neutral"))
    return trend


def correlate_with_bot_signals(df: pd.DataFrame, bot_signals: pd.Series) -> pd.Series:
    """
    Corrèle les tendances intraday avec les signaux du bot.
    
    Paramètres :
    - df : DataFrame contenant ['timestamp']
    - bot_signals : Série indexée par timestamp avec signaux du bot
    
    Retour :
    - Série booléenne indiquant si la tendance est alignée avec le bot
    """
    alignment = []
    for ts, trend in zip(df["timestamp"], df["Trend"]):
        bot_signal = bot_signals.get(ts, None)
        alignment.append(trend == bot_signal)
    return pd.Series(alignment, index=df.index)


def filter_intraday(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applique des filtres intraday (ex. news impactantes, setups directionnels).
    
    Paramètres :
    - df : DataFrame contenant ['Trend','NewsImpact']
    
    Retour :
    - DataFrame filtré
    """
    filtered = []
    for _, row in df.iterrows():
        if row.get("NewsImpact", False):
            continue  # filtrer news impactantes
        if row["Trend"] == "Bullish" and row.get("TooDirectional", False):
            continue  # trop directionnel pour un setup range
        filtered.append(row)
    return pd.DataFrame(filtered)
