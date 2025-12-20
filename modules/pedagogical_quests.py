# ✅ Logique de quête pédagogique
# 🎯 Objectif : Proposer à l’élève des quêtes pédagogiques :
# Objectifs clairs, Récompenses à la clé, Narration motivante, Suivi de progression
def get_available_quests(user_name, feedback_df, memory_dict):
    """
    Génère des quêtes pédagogiques personnalisées.
    """
    valides = feedback_df[(feedback_df["user"] == user_name) & (feedback_df["decision"] == "Valider")].shape[0]
    weak_scenarios = [s for s, score in memory_dict.items() if score < 0]

    quests = []

    if valides < 10:
        quests.append({"titre": "Premiers pas", "objectif": "Valider 10 signaux", "récompense": "📈 Progression Active"})
    if weak_scenarios:
        quests.append({"titre": "Réhabilitation", "objectif": f"Revalider 3 scénarios faibles : {', '.join(weak_scenarios[:3])}", "récompense": "🔄 Badge de persévérance"})
    quests.append({"titre": "Exploration", "objectif": "Tester 5 scénarios différents", "récompense": "🧭 Badge Explorateur"})

    return quests
