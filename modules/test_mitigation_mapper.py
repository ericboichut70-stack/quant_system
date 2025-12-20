import pandas as pd
from mitigation_mapper import detect_mitigation_zones, summarize_mitigation

df_candles = pd.DataFrame([
    {"open": 100, "high": 105, "low": 95, "close": 102},
    {"open": 103, "high": 108, "low": 100, "close": 107},
    {"open": 110, "high": 115, "low": 109, "close": 114},  # Bullish (low=109 > high[i-2]=105)
    {"open": 112, "high": 113, "low": 90,  "close": 92},   # Bearish (high=113 < low[i-2]=95)
])

result = detect_mitigation_zones(df_candles)
print(result[["open","high","low","close","MitigationZone"]])
print(summarize_mitigation(result))
