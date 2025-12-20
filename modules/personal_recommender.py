# ✅ Module de recommandation personnalisée
def recommend_scenarios(feedback_df, memory_dict, user_name, min_score=0):
    """
    Recommande des scénarios à un élève selon son historique et sa mémoire.
    """
    user_df = feedback_df[feedback_df["user"] == user_name]
    validated = user_df[user_df["decision"] == "Valider"]["ScenarioType"].value_counts()

    recommendations = []
    for scenario, count in validated.items():
        mem_score = memory_dict.get(scenario, 0)
        if mem_score >= min_score:
            recommendations.append((scenario, count, mem_score))

    recommendations.sort(key=lambda x: (-x[1], -x[2]))  # Priorité : validation fréquente + mémoire forte
    return recommendations
