import pandas as pd

def detect_liquidity_zones(df: pd.DataFrame, window: int = 20, sensitivity: float = 0.8) -> pd.DataFrame:
    """
    Détecte les zones de liquidité selon la densité des prix.
    Retourne un DataFrame avec une colonne 'LiquidityZone' : 'low', 'high', 'neutral'
    """
    df = df.copy()
    df["MidPrice"] = (df["high"] + df["low"]) / 2

    # Histogramme des prix moyens
    price_bins = pd.cut(df["MidPrice"], bins=30)
    zone_density = price_bins.value_counts(normalize=True)

    # Seuils
    high_threshold = zone_density.max() * sensitivity
    low_threshold = zone_density.max() * (1 - sensitivity)

    df["LiquidityZone"] = "neutral"
    for zone, density in zone_density.items():
        if density >= high_threshold:
            df.loc[price_bins == zone, "LiquidityZone"] = "high"
        elif density <= low_threshold:
            df.loc[price_bins == zone, "LiquidityZone"] = "low"

    return df
