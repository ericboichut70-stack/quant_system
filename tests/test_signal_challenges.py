# 🧪 Test signal_challenges avec plusieurs niveaux
from modules.signal_challenges import generate_challenge, assign_level

scenarios = [
    {"ScenarioType": "breaker", "Score": 92},
    {"ScenarioType": "sweep", "Score": 76},
    {"ScenarioType": "mitigation", "Score": 64},
    {"ScenarioType": "range", "Score": 58}
]

print("🎮 Test signal_challenges")
for s in scenarios:
    level = assign_level(s["Score"])
    challenge = generate_challenge(s["ScenarioType"], level)
    print(f"{s['ScenarioType']} | Score: {s['Score']} → Niveau: {level} | Défi : {challenge}")
