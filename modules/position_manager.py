# modules/position_manager.py

import pandas as pd

def calculate_position_size(capital: float, risk_pct: float, atr: float) -> int:
    """
    Calcule la taille de position optimale en fonction du capital, du risque et de l'ATR.
    
    Paramètres :
    - capital : capital disponible
    - risk_pct : pourcentage de risque par trade (ex. 0.01 = 1%)
    - atr : Average True Range (volatilité moyenne)
    
    Retour :
    - Taille de la position (nombre d’unités)
    """
    risk_amount = capital * risk_pct
    if atr <= 0:
        return 0
    size = int(risk_amount / (atr * 2))  # SL = ATR*2
    return max(size, 0)


def manage_positions(df: pd.DataFrame, capital: float = 100000, risk_pct: float = 0.01) -> pd.DataFrame:
    """
    Ajoute une colonne 'PositionSize' aux signaux en fonction du capital et de l’ATR.
    
    Paramètres :
    - df : DataFrame contenant au minimum ['timestamp','ATR']
    - capital : capital fictif (par défaut 100000)
    - risk_pct : pourcentage de risque par trade (par défaut 1%)
    
    Retour :
    - DataFrame enrichi avec 'PositionSize'
    """
    df = df.copy()
    df["PositionSize"] = df["ATR"].apply(lambda atr: calculate_position_size(capital, risk_pct, atr))
    return df
