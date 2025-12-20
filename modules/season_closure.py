# 🎉 Interface de célébration de fin de saison
# 🎯 Objectif : Célébrer la fin d’une saison en :
# Affichant les trophées, badges et classements, Remerciant les participants, Proposant une transition vers la prochaine saison
def generate_season_closure(active_season, trophy, ranking_df, badge_log):
    """
    Génère un message de clôture de saison.
    """
    top_user = trophy["Utilisateur"]
    top_score = trophy["Score"]
    season_name = active_season["name"]

    closure = [
        f"🎉 Fin de la saison **{season_name}** !",
        f"🏆 Trophée communautaire attribué à **{top_user}** avec {top_score} validations.",
        f"📊 Classement final :",
        ranking_df.to_markdown(index=False),
        f"🏅 Badges attribués : {badge_log['badge'].nunique()} types, {badge_log['user'].nunique()} membres récompensés.",
        "🚀 Préparez-vous pour la prochaine saison… de nouvelles quêtes arrivent !"
    ]
    return "\n\n".join(closure)
