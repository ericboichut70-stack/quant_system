import pandas as pd
from datetime import timedelta

# Chargement du calendrier économique
def load_news_calendar(path, impact_filter="high"):
    df = pd.read_csv(path, parse_dates=["timestamp"])
    if impact_filter:
        df = df[df["impact"].str.lower() == impact_filter.lower()]
    return df

# Détection de news proches d’un signal
def is_near_news(signal_time, news_df, window_minutes=30):
    delta = timedelta(minutes=window_minutes)
    return any(abs(signal_time - news_time) <= delta for news_time in news_df["timestamp"])

# Calcul d’un indice de turbulence basé sur la volatilité
def compute_turbulence_index(df, window=15):
    df["volatility"] = df["High"] - df["Low"]
    df["turbulence"] = df["volatility"].rolling(window).std()
    return df
