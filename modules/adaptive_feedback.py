# ✅ Logique de feedback adaptatif en temps réel
def generate_adaptive_feedback(signal_row, user_name, memory_dict, settings):
    """
    Génère un feedback pédagogique adaptatif en temps réel.
    """
    scenario = signal_row["ScenarioType"]
    score = signal_row["ConfidenceScore"]
    mem_score = memory_dict.get(scenario, 0)

    feedback = []

    if score < 3:
        feedback.append(f"⚠️ Score faible pour '{scenario}' — à éviter sauf justification.")
    elif score > 7:
        feedback.append(f"✅ Signal fort pour '{scenario}' — bon candidat à validation.")

    if mem_score < -2:
        feedback.append(f"🔻 Ce scénario est désactivé — attention à sa fiabilité.")
    elif mem_score > 5:
        feedback.append(f"📈 Scénario bien maîtrisé — tu peux approfondir.")

    if "Diversité" in settings["focus"]:
        feedback.append(f"🎨 Pense à varier les scénarios pour enrichir ton apprentissage.")

    return " ".join(feedback)
