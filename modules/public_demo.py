# 🌐 Interface publique de démonstration
# 🎯 Objectif : Permettre à un utilisateur invité ou non mentoré de :
# Tester le bot en mode basique, Visualiser un parcours simulé,
# Recevoir un feedback sans activation réelle, Découvrir les modules pédagogiques sans engagement
def public_demo_interface(signal_row, demo_memory_dict):
    """
    Interface publique de démonstration pédagogique.
    """
    scenario = signal_row["ScenarioType"]
    score = signal_row["ConfidenceScore"]
    mem_score = demo_memory_dict.get(scenario, 0)

    feedback = []
    feedback.append(f"🎭 Démo du scénario '{scenario}' avec score {score}")

    if mem_score < 0:
        feedback.append("🔻 Ce scénario est désactivé dans la version pédagogique.")
    elif mem_score > 5:
        feedback.append("📈 Scénario bien maîtrisé — recommandé en version mentorée.")

    feedback.append("🧠 Ce signal est simulé. Aucun risque, aucun engagement.")

    return " ".join(feedback)
