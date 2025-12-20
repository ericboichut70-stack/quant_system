import pandas as pd

from modules.trend_detector import detect_trend
from modules.volatility_clustering import detect_volatility_clusters
from modules.zigzag_mapper import compute_zigzag
from modules.structure_tracker import detect_market_structure
from modules.orderflow_reader import compute_orderflow
from modules.signal_predictor import extract_features, enrich_features, predict_signals
from modules.optimizer import optimize_parameters, apply_optimized_parameters
from modules.signal_attribution import attribute_signals
from modules.signature_generator import add_signatures
from modules.trading_api import place_order

# ============================================================
# 1. Données fictives
# ============================================================

df = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","open":100,"high":105,"low":95,"close":100,"volume":800,
     "buy_volume":500,"sell_volume":300},
    {"timestamp":"2025-12-16 09:15:00","open":100,"high":106,"low":99,"close":102,"volume":1200,
     "buy_volume":800,"sell_volume":900},
    {"timestamp":"2025-12-16 09:30:00","open":102,"high":103,"low":95,"close":101,"volume":900,
     "buy_volume":1200,"sell_volume":1100},
    {"timestamp":"2025-12-16 09:45:00","open":101,"high":107,"low":100,"close":105,"volume":1500,
     "buy_volume":1500,"sell_volume":1400},
])

# ============================================================
# 2. Analyse de marché
# ============================================================

df = detect_trend(df)
df = detect_volatility_clusters(df)
df = compute_zigzag(df)
df = detect_market_structure(df)
df = compute_orderflow(df)

# ============================================================
# 3. Prédiction de signaux
# ============================================================

df = extract_features(df)
df = enrich_features(df)
df = predict_signals(df)

# ============================================================
# 4. Optimisation
# ============================================================

params = optimize_parameters(df)
df = apply_optimized_parameters(df, params)

# ============================================================
# 5. Attribution & signature
# ============================================================

df = attribute_signals(df)
df = add_signatures(df)

# ============================================================
# 6. Exécution simulée
# ============================================================

final_signal = df["ConvergentSignal"].iloc[-1]

if final_signal == "Buy":
    order = place_order("BTCUSD", "Buy", 0.1, df["close"].iloc[-1])
elif final_signal == "Sell":
    order = place_order("BTCUSD", "Sell", 0.1, df["close"].iloc[-1])
else:
    order = {"status": "No trade"}

print("\n=== PIPELINE COMPLET ===")
print(df)
print("\n=== ORDRE FINAL ===")
print(order)
