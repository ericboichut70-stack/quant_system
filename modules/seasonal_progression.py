# 🌱 Logique de progression par saison
# 🎯 Objectif : Structurer la progression pédagogique en saisons thématiques :
# Chaque saison a ses scénarios, défis, badges;
# L’élève progresse dans une saison avant de débloquer la suivante, Permet une narration cyclique et renouvelable
def assign_season(feedback_df, user_name):
    """
    Attribue une saison pédagogique à un élève selon sa progression.
    """
    valides = (feedback_df[(feedback_df["user"] == user_name)]["decision"] == "Valider").sum()

    if valides < 10:
        return "🌱 Saison 1 — Initiation"
    elif valides < 30:
        return "🔥 Saison 2 — Consolidation"
    elif valides < 60:
        return "🌪️ Saison 3 — Maîtrise"
    else:
        return "🌟 Saison 4 — Transmission"
