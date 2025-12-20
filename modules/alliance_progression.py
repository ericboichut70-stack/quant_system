# ✅ Logique de progression par alliance
# 🎯 Objectif : Permettre à un binôme ou groupe d’élèves de :
# Progresser ensemble, Débloquer des quêtes collectives, Recevoir des récompenses partagées
def alliance_progress(feedback_df, alliance_members):
    """
    Calcule la progression collective d’une alliance.
    """
    import pandas as pd

    alliance_df = feedback_df[feedback_df["user"].isin(alliance_members)]
    total_validations = (alliance_df["decision"] == "Valider").sum()
    shared_scenarios = alliance_df["ScenarioType"].value_counts().head(3).index.tolist()

    if total_validations >= 50:
        badge = "🏅 Alliance Confirmée"
    elif total_validations >= 20:
        badge = "📈 Alliance Active"
    else:
        badge = "🌱 Alliance en formation"

    return {
        "Total validations": total_validations,
        "Scénarios dominants": shared_scenarios,
        "Badge collectif": badge
    }
