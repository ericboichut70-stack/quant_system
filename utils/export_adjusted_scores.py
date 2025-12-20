# 📊 Export .csv des scores ajustés
import pandas as pd
from modules.memory_evolution import apply_memory_to_score

def export_adjusted_scores():
    memory_dict = {"breaker": 3, "sweep": -4, "mitigation": 0, "imbalance": 2}
    scenarios = [
        {"ScenarioType": "breaker", "ConfidenceScore": 78},
        {"ScenarioType": "sweep", "ConfidenceScore": 72},
        {"ScenarioType": "mitigation", "ConfidenceScore": 65},
        {"ScenarioType": "imbalance", "ConfidenceScore": 80}
    ]

    data = []
    for row in scenarios:
        adjusted = apply_memory_to_score(row["ConfidenceScore"], row["ScenarioType"], memory_dict)
        data.append({
            "ScenarioType": row["ScenarioType"],
            "BaseScore": row["ConfidenceScore"],
            "MemoryBoost": memory_dict.get(row["ScenarioType"], 0),
            "AdjustedScore": adjusted
        })

    df = pd.DataFrame(data)
    df.to_csv("exports/adjusted_scores.csv", index=False)
    print("✅ Export CSV généré : adjusted_scores.csv")

if __name__ == "__main__":
    export_adjusted_scores()
