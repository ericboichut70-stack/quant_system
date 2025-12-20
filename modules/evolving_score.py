# ✅ Logique de score collectif évolutif
def compute_evolving_score(feedback_df, cross_df, auto_df, coherence_df):
    """
    Calcule un score collectif évolutif pour chaque scénario.
    """
    mentor_validations = feedback_df[feedback_df["decision"] == "Valider"]["ScenarioType"].value_counts()
    parrain_validations = cross_df[cross_df["decision"] == "Valider"]["scenario"].value_counts()
    bot_validations = auto_df[auto_df["AutoDecision"] == "Valider"]["ScenarioType"].value_counts()
    coherence_scores = coherence_df["Cohérence (%)"]

    all_scenarios = set(mentor_validations.index) | set(parrain_validations.index) | set(bot_validations.index)

    score_data = []
    for scenario in all_scenarios:
        m = mentor_validations.get(scenario, 0)
        p = parrain_validations.get(scenario, 0)
        b = bot_validations.get(scenario, 0)
        c = coherence_scores.get(scenario, 0)
        score = round((m + p + b) * (c / 100), 2)
        score_data.append({"ScenarioType": scenario, "Score collectif évolutif": score})

    return pd.DataFrame(score_data).sort_values("Score collectif évolutif", ascending=False)
