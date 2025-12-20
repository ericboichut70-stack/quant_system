# 🧪 Logique de simulation pré-trade
def simulate_signal(signal_row, memory_dict, user_settings):
    """
    Simule un signal sans activation réelle.
    """
    scenario = signal_row["ScenarioType"]
    score = signal_row["ConfidenceScore"]
    mem_score = memory_dict.get(scenario, 0)

    feedback = []
    feedback.append(f"🧪 Simulation du scénario '{scenario}' avec score {score}")

    if mem_score < 0:
        feedback.append("🔻 Ce scénario est actuellement désactivé.")
    elif mem_score > 5:
        feedback.append("📈 Scénario bien maîtrisé — simulation recommandée.")

    if "Validation" in user_settings["focus"]:
        feedback.append("🧠 Ce signal pourrait être validé en réel.")

    return " ".join(feedback)
