# 🧪 Générer un test trend_detector avec DataFrame simulé
import pandas as pd
from modules.trend_detector import detect_trend

# Données simulées
df = pd.DataFrame({
    "close": [1.1000, 1.1015, 1.1020, 1.1005, 1.0990, 1.0985, 1.0995, 1.1005],
    "high":  [1.1010, 1.1020, 1.1030, 1.1010, 1.1000, 1.0990, 1.1000, 1.1010],
    "low":   [1.0990, 1.1005, 1.1010, 1.0995, 1.0980, 1.0975, 1.0985, 1.0995]
})

result = detect_trend(df)
print(result[["close", "TrendCode"]])

# 📤 Export .csv des tendances détectées
result.to_csv("exports/trend_detector_output.csv", index=False)
print("✅ Export CSV généré : trend_detector_output.csv")
