import pandas as pd
from quantum_bridge import build_quantum_bridge, summarize_bridge

# --- Création de deux DataFrames fictifs ---
df1 = pd.DataFrame([
    {"timestamp":"2025-12-16 10:00:00","Signal":"Buy","Strength":0.8},
    {"timestamp":"2025-12-16 11:00:00","Signal":"Sell","Strength":0.6},
])

df2 = pd.DataFrame([
    {"timestamp":"2025-12-16 10:30:00","Signal":"Buy","Strength":0.9},
    {"timestamp":"2025-12-16 11:30:00","Signal":"Hold","Strength":0.4},
])

# --- Construction du bridge ---
bridge = build_quantum_bridge([df1, df2])
print("Bridge consolidé :")
print(bridge)

# --- Résumé ---
print("\nRésumé du bridge :")
print(summarize_bridge(bridge))
