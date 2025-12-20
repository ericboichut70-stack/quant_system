import pandas as pd
from signature_generator import generate_signature, add_signatures

# --- DataFrame fictif ---
df_signals = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","Signal":"Buy","Price":100,"Strength":0.8},
    {"timestamp":"2025-12-16 09:15:00","Signal":"Sell","Price":102,"Strength":0.6},
])

# --- Test de génération simple ---
sig = generate_signature(df_signals.iloc[0].to_dict())
print("Signature simple :", sig)

# --- Test d'ajout de signatures ---
df_signed = add_signatures(df_signals)
print("\nDataFrame enrichi :")
print(df_signed)
