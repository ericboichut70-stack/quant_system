# ✅ Interface de récompense collective
# 🎯 Objectif : Attribuer une récompense partagée à un binôme ou groupe selon :
# Validations cumulées, Scénarios communs, Engagement croisé
def assign_collective_reward(feedback_df, members):
    """
    Attribue une récompense collective à un groupe d’élèves.
    """
    group_df = feedback_df[feedback_df["user"].isin(members)]
    total_validations = (group_df["decision"] == "Valider").sum()
    shared_scenarios = group_df["ScenarioType"].value_counts().head(2).index.tolist()

    if total_validations >= 50:
        reward = "🏅 Badge 'Alliance Confirmée'"
    elif total_validations >= 20:
        reward = "📈 Badge 'Alliance Active'"
    else:
        reward = "🌱 Badge 'Alliance en formation'"

    return {
        "Membres": members,
        "Validations": total_validations,
        "Scénarios communs": shared_scenarios,
        "Récompense collective": reward
    }
