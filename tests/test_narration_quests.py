# 🧪 Test narration_quests avec plusieurs scénarios
from modules.narration_quests import generate_quest, assign_badge

scenarios = [
    {"ScenarioType": "breaker", "Score": 92},
    {"ScenarioType": "sweep", "Score": 76},
    {"ScenarioType": "mitigation", "Score": 64},
    {"ScenarioType": "imbalance", "Score": 58}
]

print("🎮 Test narration_quests")
for s in scenarios:
    quest = generate_quest(s["ScenarioType"], s["Score"])
    badge = assign_badge(s["Score"])
    print(f"{s['ScenarioType']} | Score: {s['Score']} → {badge} | {quest}")
