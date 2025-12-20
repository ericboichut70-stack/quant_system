# modules/signal_predictor.py

import pandas as pd
import numpy as np

def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extrait des features simples pour la prédiction de signaux.

    Paramètres :
    - df : DataFrame contenant ['timestamp','open','high','low','close','volume']

    Retour :
    - DataFrame enrichi avec colonnes :
      * 'Return' : variation relative du close
      * 'Volatility' : amplitude high-low
      * 'VolumeNorm' : volume normalisé
    """
    df = df.copy()
    df["Return"] = df["close"].pct_change().fillna(0)
    df["Volatility"] = (df["high"] - df["low"]) / df["close"]
    df["VolumeNorm"] = df["volume"] / df["volume"].rolling(5).mean().fillna(df["volume"])
    return df


def enrich_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Enrichit les features avec des indicateurs supplémentaires.

    Paramètres :
    - df : DataFrame enrichi par extract_features

    Retour :
    - DataFrame enrichi avec colonnes :
      * 'EMA' : moyenne exponentielle du close
      * 'Momentum' : différence du close sur 3 périodes
    """
    df = df.copy()
    df["EMA"] = df["close"].ewm(span=5).mean()
    df["Momentum"] = df["close"].diff(3).fillna(0)
    return df


def predict_signals(df: pd.DataFrame, threshold: float = 0.01) -> pd.DataFrame:
    """
    Prédit des signaux simples à partir des features.

    Paramètres :
    - df : DataFrame enrichi par enrich_features
    - threshold : seuil de variation pour générer un signal

    Retour :
    - DataFrame enrichi avec colonne 'PredictedSignal' :
      * 'Buy' si Return > threshold et Momentum > 0
      * 'Sell' si Return < -threshold et Momentum < 0
      * 'Hold' sinon
    """
    df = df.copy()
    df["PredictedSignal"] = "Hold"

    for i, row in df.iterrows():
        if row["Return"] > threshold and row["Momentum"] > 0:
            df.at[i, "PredictedSignal"] = "Buy"
        elif row["Return"] < -threshold and row["Momentum"] < 0:
            df.at[i, "PredictedSignal"] = "Sell"

    return df
