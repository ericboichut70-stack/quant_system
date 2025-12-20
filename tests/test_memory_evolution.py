# 🧪 Test memory_evolution avec plusieurs scénarios
from modules.memory_evolution import apply_memory_to_score, suggest_adjustments_from_memory

memory_dict = {
    "breaker": 3,
    "sweep": -4,
    "mitigation": 0,
    "imbalance": 2
}

scenarios = [
    {"ScenarioType": "breaker", "ConfidenceScore": 78},
    {"ScenarioType": "sweep", "ConfidenceScore": 72},
    {"ScenarioType": "mitigation", "ConfidenceScore": 65},
    {"ScenarioType": "imbalance", "ConfidenceScore": 80}
]

print("🧠 Test memory_evolution")
for row in scenarios:
    adjusted = apply_memory_to_score(row["ConfidenceScore"], row["ScenarioType"], memory_dict)
    print(f"{row['ScenarioType']} | Base: {row['ConfidenceScore']} → Ajusté: {adjusted}")

print("\n📋 Suggestions pédagogiques :")
for s in suggest_adjustments_from_memory(memory_dict):
    print(s)
