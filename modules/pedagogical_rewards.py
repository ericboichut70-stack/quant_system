# 🏅 Module de récompense pédagogique
# 🎯 Objectif : Attribuer des récompenses pédagogiques selon :
# Progression individuelle, Score binôme, Participation à des défis ou tournois, Engagement communautaire
def assign_rewards(feedback_df, binome_scores, tournament_df, user_name):
    """
    Attribue des récompenses pédagogiques à un élève.
    """
    rewards = []

    valides = feedback_df[(feedback_df["user"] == user_name) & (feedback_df["decision"] == "Valider")].shape[0]
    binome_score = binome_scores[binome_scores["Binôme"].str.contains(user_name)]["Score binôme"].max()
    tournament_score = tournament_df[tournament_df["Participant"] == user_name]["Score"].max()

    if valides >= 30:
        rewards.append("🎓 Badge 'Validation Expert'")
    if binome_score and binome_score > 50:
        rewards.append("🤝 Badge 'Binôme d’Or'")
    if tournament_score and tournament_score > 20:
        rewards.append("🏆 Badge 'Champion de Tournoi'")
    if valides >= 10 and not rewards:
        rewards.append("📈 Badge 'Progression Active'")

    return rewards
