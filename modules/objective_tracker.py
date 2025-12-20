# ✅ Module de suivi des objectifs
def track_objectives(feedback_df, user_name, settings):
    """
    Suit la progression d’un élève selon ses objectifs pédagogiques.
    """
    user_df = feedback_df[feedback_df["user"] == user_name]
    total = len(user_df)
    valides = (user_df["decision"] == "Valider").sum()
    ratio = round(valides / total * 100, 2) if total else 0

    scenario_diversity = user_df["ScenarioType"].nunique()
    coherence = ratio if "Cohérence" in settings["focus"] else None
    autonomy = total if settings["mode"] == "Autonome" else None

    return {
        "Total signaux": total,
        "Validés": valides,
        "Taux de validation (%)": ratio,
        "Scénarios différents": scenario_diversity,
        "Cohérence (%)": coherence,
        "Autonomie (signaux soumis)": autonomy
    }
