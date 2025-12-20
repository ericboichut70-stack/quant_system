# 🏅 Logique de badge communautaire
# 🎯 Objectif : Attribuer des badges communautaires selon :
# Contribution à une saison, Participation à des défis collectifs, Engagement dans les validations croisées
def assign_community_badges(feedback_df, user_name, season_scenarios):
    """
    Attribue des badges communautaires à un utilisateur.
    """
    user_df = feedback_df[(feedback_df["user"] == user_name) & (feedback_df["ScenarioType"].isin(season_scenarios))]
    valides = (user_df["decision"] == "Valider").sum()

    badges = []
    if valides >= 30:
        badges.append("🏅 Badge 'Pilier de saison'")
    elif valides >= 15:
        badges.append("📈 Badge 'Contributeur actif'")
    elif valides >= 5:
        badges.append("🌱 Badge 'Participant engagé'")
    else:
        badges.append("👀 Badge 'Observateur'")

    return badges
