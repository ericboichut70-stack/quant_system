import numpy as np
import pandas as pd
from datetime import datetime, time
from typing import Dict, List, Tuple, Union


def calculate_ut_pivots(
    df: pd.DataFrame,
    calculation_hour: int = 22,
    lookback_period: int = 114,  # 6 * 19 = 114 (référence au Coran)
    golden_ratio: float = 1.618,
    num_levels: int = 4
) -> Dict[str, float]:
    """
    Calcule les niveaux des Pivots d'UT (UT Pivots) basés sur le centre de gravité et le ratio d'or.
    
    Args:
        df: DataFrame pandas avec les colonnes ['open', 'high', 'low', 'close', 'timestamp']
        calculation_hour: Heure (UTC) à laquelle les pivots sont calculés (par défaut 22h00)
        lookback_period: Période de lookback pour la régression (par défaut 114, multiple de 19)
        golden_ratio: Ratio d'or utilisé pour les multiplicateurs (par défaut 1.618)
        num_levels: Nombre de niveaux de support/résistance de chaque côté du pivot
        
    Returns:
        Un dictionnaire contenant les niveaux de support (S1-S4), le pivot (P) et les résistances (R1-R4)
    """
    # Vérification des données d'entrée
    required_columns = ['open', 'high', 'low', 'close', 'timestamp']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Le DataFrame doit contenir les colonnes: {required_columns}")
    
    # Conversion de la colonne timestamp si nécessaire
    if not pd.api.types.is_datetime64_any_dtype(df['timestamp']):
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Trier par date (plus ancien au plus récent)
    df = df.sort_values('timestamp')
    
    # Filtrer les données jusqu'à l'heure de calcul de la veille
    last_date = df['timestamp'].max()
    if last_date.hour < calculation_hour:
        # Si on n'a pas encore atteint l'heure de calcul, on prend la veille
        last_date = last_date - pd.Timedelta(days=1)
    
    # Créer un masque pour les données jusqu'à l'heure de calcul
    mask = (df['timestamp'].dt.date < last_date.date()) | \
           ((df['timestamp'].dt.date == last_date.date()) & 
            (df['timestamp'].dt.hour < calculation_hour))
    
    # Prendre les N dernières périodes qui correspondent au masque
    filtered_df = df[mask].tail(lookback_period)
    
    if len(filtered_df) < 2:
        raise ValueError("Pas assez de données pour calculer les pivots")
    
    # Calcul du centre de gravité avec régression polynomiale
    x = np.arange(len(filtered_df))
    y = filtered_df['close'].values
    
    # Régression polynomiale de degré 3
    coeffs = np.polyfit(x, y, 3)
    poly = np.poly1d(coeffs)
    
    # Calcul des valeurs prédites et des résidus
    y_pred = poly(x)
    residuals = y - y_pred
    
    # Calcul de l'écart-type des résidus (sigma)
    sigma = np.std(residuals)
    
    # Dernière valeur du polynôme comme centre
    center = float(poly(len(filtered_df) - 1))
    
    # Calcul des niveaux de support et résistance
    levels = {}
    
    # Pivot central
    levels['P'] = center
    
    # Calcul des niveaux de support (S) et résistance (R)
    for i in range(1, num_levels + 1):
        # Calcul des multiplicateurs basés sur le nombre d'or et le nombre 19
        # On utilise la formule: (golden_ratio ** (i-1)) * (1 + (i % 3) * 0.19)
        multiplier = (golden_ratio ** (i-1)) * (1 + (i % 3) * 0.19)
        
        # Niveaux de support (négatifs)
        s_key = f'S{i}'
        levels[s_key] = center - (multiplier * sigma)
        
        # Niveaux de résistance (positifs)
        r_key = f'R{i}'
        levels[r_key] = center + (multiplier * sigma)
    
    # Trier les niveaux par ordre croissant
    sorted_levels = dict(sorted(levels.items(), key=lambda item: item[1]))
    
    # Formater les niveaux avec 5 décimales
    return {k: round(v, 5) for k, v in sorted_levels.items()}


def generate_sample_data(days: int = 30, timeframe: str = '15T') -> pd.DataFrame:
    """
    Génère des données OHLC factices pour le test de l'indicateur.
    
    Args:
        days: Nombre de jours de données à générer
        timeframe: Intervalle de temps (par défaut '15T' pour 15 minutes)
        
    Returns:
        DataFrame avec des données OHLC factices
    """
    np.random.seed(42)  # Pour la reproductibilité
    
    # Créer un index de temps
    end_date = datetime.now()
    start_date = end_date - pd.Timedelta(days=days)
    date_range = pd.date_range(start=start_date, end=end_date, freq=timeframe)
    
    # Générer des prix aléatoires avec une tendance légèrement haussière
    n = len(date_range)
    base = np.linspace(1.08, 1.12, n)  # Tendance linéaire
    noise = np.random.normal(0, 0.002, n)  # Bruit aléatoire
    close_prices = base + noise
    
    # Générer OHLC à partir des prix de clôture
    df = pd.DataFrame(index=date_range, columns=['open', 'high', 'low', 'close'])
    df['close'] = close_prices
    
    # Générer des bougies réalistes
    df['returns'] = np.random.normal(0, 0.001, n)
    df['close'] = (1 + df['returns']).cumprod() * 1.08
    df['open'] = df['close'].shift(1) * (1 + np.random.normal(0, 0.0005, n))
    df['high'] = df[['open', 'close']].max(axis=1) * (1 + np.abs(np.random.normal(0, 0.0005, n)))
    df['low'] = df[['open', 'close']].min(axis=1) * (1 - np.abs(np.random.normal(0, 0.0005, n)))
    
    # Supprimer les valeurs NaN et réinitialiser l'index
    df = df.dropna()
    df = df.reset_index().rename(columns={'index': 'timestamp'})
    
    return df[['timestamp', 'open', 'high', 'low', 'close']]


if __name__ == "__main__":
    # Exemple d'utilisation
    print("Génération de données d'exemple...")
    sample_data = generate_sample_data(days=60)  # 60 jours de données
    
    print("\nCalcul des niveaux de Ballistic Pivots...")
    try:
        pivots = calculate_ut_pivots(sample_data)
        
        print("\nNiveaux de Ballistic Pivots:")
        for level, value in pivots.items():
            print(f"{level}: {value:.5f}")
            
    except Exception as e:
        print(f"\nErreur lors du calcul des pivots: {str(e)}")

# 🔧 Couleur bande centrale UT Pivots
def detect_pivot_band(df):
    """
    Détecte la bande entre deux pivots encadrant le pivot central.
    Retourne 'bullish', 'bearish' ou 'neutral' selon la couleur dominante.
    """
    if "PivotHigh" not in df or "PivotLow" not in df or "PivotCentral" not in df:
        return "neutral"

    # Exemple : si le pivot central est plus proche du haut et le volume est en hausse
    if df["PivotCentral"].mean() > df["PivotLow"].mean() and df["Volume"].mean() > df["Volume"].rolling(10).mean().mean():
        return "bullish"
    elif df["PivotCentral"].mean() < df["PivotHigh"].mean() and df["Volume"].mean() < df["Volume"].rolling(10).mean().mean():
        return "bearish"
    return "neutral"
