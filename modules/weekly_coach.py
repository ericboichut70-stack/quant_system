# ✅ Interface de coaching hebdomadaire
def weekly_coaching(feedback_df, user_name, memory_dict, settings):
    """
    Génère un bilan hebdomadaire personnalisé.
    """
    user_df = feedback_df[feedback_df["user"] == user_name]
    recent = user_df[user_df["timestamp"] >= pd.Timestamp.now() - pd.Timedelta("7D")]

    total = len(recent)
    valides = (recent["decision"] == "Valider").sum()
    top_scenarios = recent["ScenarioType"].value_counts().head(3).index.tolist()

    recommendations = [s for s in top_scenarios if memory_dict.get(s, 0) >= 0]

    return {
        "Total signaux soumis": total,
        "Validés cette semaine": valides,
        "Scénarios dominants": top_scenarios,
        "Recommandations ciblées": recommendations
    }
