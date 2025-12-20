# ✅ 3. Simulation collective
# 🎯 Objectif : Permettre à plusieurs élèves de : Simuler des signaux en parallèle,
# Comparer leurs décisions, Recevoir un feedback croisé, Créer un défi ou tournoi pédagogique
def simulate_group_signals(group_signals, memory_dict):
    """
    Simule les signaux d’un groupe d’élèves.
    """
    results = []

    for signal in group_signals:
        user = signal["user"]
        scenario = signal["ScenarioType"]
        score = signal["ConfidenceScore"]
        mem_score = memory_dict.get(scenario, 0)

        feedback = f"{user} → {scenario} ({score}) : "
        if mem_score < 0:
            feedback += "🔻 Scénario désactivé"
        elif score > 7:
            feedback += "✅ Signal fort"
        else:
            feedback += "🧪 Signal modéré"

        results.append(feedback)

    return results
