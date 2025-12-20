# ✅ Progression scénarisée par groupe
# 🎯 Objectif : Permettre à un groupe d’élèves de suivre un parcours pédagogique commun,
# avec: Scénarios partagés, Objectifs collectifs, Suivi croisé
def build_group_pathway(feedback_df, group_members):
    """
    Génère un parcours scénarisé pour un groupe d’élèves.
    """
    import pandas as pd

    group_df = feedback_df[feedback_df["user"].isin(group_members)]
    scenario_stats = group_df["ScenarioType"].value_counts().to_frame(name="Occurrences")
    validations = group_df[group_df["decision"] == "Valider"]["ScenarioType"].value_counts().to_frame(name="Validations")

    pathway_df = scenario_stats.join(validations, how="left").fillna(0)
    pathway_df["Taux de validation"] = round(pathway_df["Validations"] / pathway_df["Occurrences"] * 100, 2)

    return pathway_df.sort_values("Taux de validation", ascending=False)
