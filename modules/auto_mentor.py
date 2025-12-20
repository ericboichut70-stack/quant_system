# 🤖 Mentorat automatique — le bot comme mentor référent
def auto_mentor_feedback(signal_row):
    """
    Génère un feedback automatique selon les règles pédagogiques du bot.
    """
    context = signal_row["ScenarioType"]
    score = signal_row["ConfidenceScore"]

    if score < 3:
        return "Rejeter", f"Score trop faible pour le scénario '{context}'"
    elif score > 7:
        return "Valider", f"Signal fort détecté pour '{context}'"
    else:
        return "À revoir", f"Signal modéré pour '{context}', nécessite confirmation"
