import pandas as pd
from packaging_module import package_signals, export_to_dataframe

# --- Création d’un DataFrame fictif ---
df_trades = pd.DataFrame([
    {"timestamp":"2025-12-16 10:00:00","Direction":"Buy","Entry":100,"Exit":110,"Size":10,"PnL":100,"Outcome":"TP"},
    {"timestamp":"2025-12-16 11:00:00","Direction":"Sell","Entry":200,"Exit":190,"Size":5,"PnL":50,"Outcome":"TP"},
    {"timestamp":"2025-12-16 12:00:00","Direction":"Buy","Entry":150,"Exit":140,"Size":8,"PnL":-80,"Outcome":"SL"},
])

# --- Paquetage ---
package = package_signals(df_trades)
print("Résumé du paquetage :")
print(package["summary"])

print("\nSignaux formatés :")
for s in package["signals"]:
    print(s)

# --- Export en DataFrame ---
df_export = export_to_dataframe(package)
print("\nDataFrame exporté :")
print(df_export)
