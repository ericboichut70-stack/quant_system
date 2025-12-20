# modules/optimizer.py

import pandas as pd
import numpy as np

def optimize_parameters(df: pd.DataFrame) -> dict:
    """
    Optimise des paramètres simples à partir d'un DataFrame de signaux ou de prix.

    Paramètres :
    - df : DataFrame contenant au minimum ['close']

    Retour :
    - Dictionnaire contenant des paramètres optimisés :
      * 'threshold'
      * 'window'
      * 'energy_filter'
    """
    volatility = df["close"].pct_change().abs().mean()
    threshold = round(volatility * 2, 4)
    window = max(3, int(len(df) * 0.1))
    energy_filter = round(df["close"].diff().abs().mean(), 4)

    return {
        "threshold": threshold,
        "window": window,
        "energy_filter": energy_filter
    }


def apply_optimized_parameters(df: pd.DataFrame, params: dict) -> pd.DataFrame:
    """
    Applique les paramètres optimisés au moteur de signaux.

    Paramètres :
    - df : DataFrame contenant ['close']
    - params : dictionnaire retourné par optimize_parameters()

    Retour :
    - DataFrame enrichi avec :
      * 'Energy' : variation absolue
      * 'Filtered' : True/False selon energy_filter
      * 'ConvergentSignal' : Buy / Sell / Hold
    """
    df = df.copy()

    # Filtrage énergie
    df["Energy"] = df["close"].diff().abs().fillna(0)
    df["Filtered"] = df["Energy"] > params["energy_filter"]

    # Générer signaux convergents
    df["ConvergentSignal"] = "Hold"
    for i, row in df.iterrows():
        if not row["Filtered"]:
            continue
        if row["close"] > df["close"].rolling(params["window"]).mean().fillna(df["close"]).iloc[i] + params["threshold"]:
            df.at[i, "ConvergentSignal"] = "Buy"
        elif row["close"] < df["close"].rolling(params["window"]).mean().fillna(df["close"]).iloc[i] - params["threshold"]:
            df.at[i, "ConvergentSignal"] = "Sell"

    return df


def summarize_optimization(df: pd.DataFrame) -> str:
    """
    Résume les signaux convergents générés par l’optimiseur.

    Paramètres :
    - df : DataFrame enrichi par apply_optimized_parameters

    Retour :
    - Chaîne descriptive indiquant le nombre de Buy / Sell / Hold
    """
    buys = (df["ConvergentSignal"] == "Buy").sum()
    sells = (df["ConvergentSignal"] == "Sell").sum()
    holds = (df["ConvergentSignal"] == "Hold").sum()

    return f"📊 Optimisation : Buy={buys}, Sell={sells}, Hold={holds}"
