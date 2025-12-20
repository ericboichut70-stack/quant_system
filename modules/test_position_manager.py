import pandas as pd
from position_manager import calculate_position_size, manage_positions

# --- Test unitaire de la fonction ---
capital = 100000
risk_pct = 0.01
atr = 50
size = calculate_position_size(capital, risk_pct, atr)
print(f"Taille de position calculée : {size}")

# --- Création d’un DataFrame fictif ---
df_signals = pd.DataFrame([
    {"timestamp":"2025-12-16 10:00:00","ATR":50},
    {"timestamp":"2025-12-16 11:00:00","ATR":30},
    {"timestamp":"2025-12-16 12:00:00","ATR":80},
])

# --- Gestion des positions ---
result = manage_positions(df_signals, capital=100000, risk_pct=0.01)
print("\nDataFrame enrichi :")
print(result)
