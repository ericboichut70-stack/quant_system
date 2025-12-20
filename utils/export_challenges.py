# 📤 Export .json des niveaux et réussites
import json
from datetime import datetime
from modules.signal_challenges import generate_challenge, assign_level

scenarios = [
    {"ScenarioType": "breaker", "Score": 92},
    {"ScenarioType": "sweep", "Score": 76},
    {"ScenarioType": "mitigation", "Score": 64},
    {"ScenarioType": "range", "Score": 58}
]

def export_challenges():
    path = "exports/challenges.json"
    data = []

    for s in scenarios:
        level = assign_level(s["Score"])
        challenge = generate_challenge(s["ScenarioType"], level)
        data.append({
            "scenario": s["ScenarioType"],
            "score": s["Score"],
            "level": level,
            "challenge": challenge,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

    with open(path, "w") as f:
        json.dump(data, f, indent=2)

    print("✅ Export JSON généré : challenges.json")

if __name__ == "__main__":
    export_challenges()
