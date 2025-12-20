# modules/volatility_clustering.py

import pandas as pd
import numpy as np

def compute_volatility(df: pd.DataFrame, period: int = 10) -> pd.Series:
    """
    Calcule la volatilité réalisée sur une fenêtre glissante.

    Paramètres :
    - df : DataFrame contenant au minimum ['close']
    - period : taille de la fenêtre pour le calcul de la volatilité

    Retour :
    - Série contenant la volatilité (écart-type des rendements)
    """
    returns = df["close"].pct_change()
    vol = returns.rolling(period).std().fillna(0)
    return vol


def detect_volatility_clusters(df: pd.DataFrame, threshold: float = 0.02) -> pd.DataFrame:
    """
    Détecte des clusters de volatilité (zones de forte ou faible volatilité).

    Paramètres :
    - df : DataFrame contenant ['timestamp','close']
    - threshold : seuil de volatilité pour distinguer HighVol / LowVol

    Retour :
    - DataFrame enrichi avec :
      * 'Volatility'
      * 'Cluster' : 'HighVol' ou 'LowVol'
    """
    df = df.copy()
    df["Volatility"] = compute_volatility(df)

    df["Cluster"] = df["Volatility"].apply(
        lambda v: "HighVol" if v > threshold else "LowVol"
    )

    return df
