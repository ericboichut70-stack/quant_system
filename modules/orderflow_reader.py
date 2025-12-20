# modules/orderflow_reader.py

import pandas as pd

def compute_orderflow(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyse l'orderflow à partir des volumes acheteurs et vendeurs.

    Paramètres :
    - df : DataFrame contenant ['timestamp','buy_volume','sell_volume','close']

    Retour :
    - DataFrame enrichi avec :
      * 'Delta' : buy_volume - sell_volume
      * 'Imbalance' : ratio d'imbalance
      * 'Absorption' : True/False (gros volume mais faible variation de prix)
    """
    df = df.copy()

    df["Delta"] = df["buy_volume"] - df["sell_volume"]
    total_vol = df["buy_volume"] + df["sell_volume"]
    df["Imbalance"] = df["Delta"] / total_vol.replace(0, 1)

    price_change = df["close"].diff().abs().fillna(0)
    df["Absorption"] = (total_vol > total_vol.mean()) & (price_change < price_change.mean())

    return df


def summarize_orderflow(df: pd.DataFrame) -> str:
    """
    Résume l'orderflow détecté.

    Paramètres :
    - df : DataFrame enrichi par compute_orderflow

    Retour :
    - Chaîne descriptive indiquant :
      * nombre d'absorptions
      * moyenne du delta
      * moyenne de l'imbalance
    """
    absorptions = df["Absorption"].sum()
    delta_mean = df["Delta"].mean()
    imbalance_mean = df["Imbalance"].mean()

    return (
        f"📊 Orderflow : absorptions={absorptions}, "
        f"delta_moyen={delta_mean:.2f}, imbalance_moyen={imbalance_mean:.2f}"
    )
