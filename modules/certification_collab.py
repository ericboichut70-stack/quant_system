# ✅ Logique de certification collaborative
def evaluate_collaborative_certification(feedback_df, cross_df, memory_dict, user_name, mentor_approval=False):
    """
    Évalue la certification collaborative d’un élève.
    """
    user_df = feedback_df[feedback_df["user"] == user_name]
    valides = (user_df["decision"] == "Valider").sum()
    cross_valides = cross_df[cross_df["user"] == user_name]
    cross_count = (cross_valides["decision"] == "Valider").sum()

    memory_scores = [memory_dict.get(s, 0) for s in user_df["ScenarioType"].unique()]
    avg_memory = round(sum(memory_scores) / len(memory_scores), 2) if memory_scores else 0

    certified = valides >= 30 and cross_count >= 10 and avg_memory >= 3 and mentor_approval

    return {
        "Validations mentorales": valides,
        "Validations croisées": cross_count,
        "Score mémoire moyen": avg_memory,
        "Certification collaborative": "✅ Oui" if certified else "❌ Non"
    }
