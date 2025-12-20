# 📤 Export .json des quêtes et badges
import json
from datetime import datetime
from modules.narration_quests import generate_quest, assign_badge

scenarios = [
    {"ScenarioType": "breaker", "Score": 92},
    {"ScenarioType": "sweep", "Score": 76},
    {"ScenarioType": "mitigation", "Score": 64},
    {"ScenarioType": "imbalance", "Score": 58}
]

def export_quests():
    path = "exports/quests_and_badges.json"
    data = []

    for s in scenarios:
        data.append({
            "scenario": s["ScenarioType"],
            "score": s["Score"],
            "badge": assign_badge(s["Score"]),
            "quest": generate_quest(s["ScenarioType"], s["Score"]),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

    with open(path, "w") as f:
        json.dump(data, f, indent=2)

    print("✅ Export JSON généré : quests_and_badges.json")

if __name__ == "__main__":
    export_quests()
