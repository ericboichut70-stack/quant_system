import pandas as pd
from orderflow_reader import compute_orderflow, summarize_orderflow

df = pd.DataFrame([
    {"timestamp":"2025-12-16 09:00:00","buy_volume":500,"sell_volume":300,"close":100},
    {"timestamp":"2025-12-16 09:15:00","buy_volume":800,"sell_volume":900,"close":101},
    {"timestamp":"2025-12-16 09:30:00","buy_volume":1200,"sell_volume":1100,"close":101},
    {"timestamp":"2025-12-16 09:45:00","buy_volume":1500,"sell_volume":1400,"close":102},
])

orderflow = compute_orderflow(df)
print("DataFrame enrichi :")
print(orderflow)

print("\nRésumé :")
print(summarize_orderflow(orderflow))
