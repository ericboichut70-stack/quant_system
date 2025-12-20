# 🧪 test_simulation.py — test inter-module pour simulation complète
from modules.trend_detector import detect_trend
from modules.auto_mentor_feedback import auto_mentor_feedback
from modules.community_scoring import aggregate_scores

import pandas as pd

print("🚀 Simulation inter-module")

# Données simulées
df = pd.DataFrame({
    "close": [1.1000, 1.1015, 1.1020, 1.1005, 1.0990, 1.0985, 1.0995, 1.1005],
    "high":  [1.1010, 1.1020, 1.1030, 1.1010, 1.1000, 1.0990, 1.1000, 1.1010],
    "low":   [1.0990, 1.1005, 1.1010, 1.0995, 1.0980, 1.0975, 1.0985, 1.0995]
})

# Détection de tendance
df = detect_trend(df)
print(df[["close", "TrendCode"]])

# Feedback mentor
scenarios = [
    {"ScenarioType": "breaker", "Score": 85},
    {"ScenarioType": "sweep", "Score": 72},
    {"ScenarioType": "mitigation", "Score": 58}
]
for s in scenarios:
    feedback = auto_mentor_feedback(s["ScenarioType"], s["Score"])
    print(f"{s['ScenarioType']} | Score: {s['Score']} → {feedback}")

# Agrégation communautaire
scores = [85, 72, 58]
role = aggregate_scores(scores)

# 📤 Export .csv des rôles attribués
import csv

with open("exports/roles_attribués.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Scores", "Rôle attribué"])
    writer.writerow([scores, role])

print(f"🎭 Rôle attribué : {role}")

# 🧠 Replay global de test_simulation.py
with open("replays/simulation_replay.txt", "w") as f:
    f.write("🚀 Simulation inter-module\n\n")
    f.write(df[["close", "TrendCode"]].to_string(index=False))
    f.write("\n\nMentor Feedback:\n")
    for s in scenarios:
        feedback = auto_mentor_feedback(s["ScenarioType"], s["Score"])
        f.write(f"{s['ScenarioType']} | Score: {s['Score']} → {feedback}\n")
    f.write(f"\n🎭 Rôle attribué : {role}\n")

print("✅ Replay global généré : simulation_replay.txt")
