# 🏆 Logique de trophée saisonnier
# 🎯 Objectif : Attribuer un trophée de fin de saison à :
# L’élève ou binôme ayant le score le plus élevé, Le contributeur le plus régulier, Le mentor ou parrain le plus actif
def assign_seasonal_trophy(feedback_df, season_scenarios, user_list):
    """
    Attribue un trophée saisonnier au meilleur contributeur.
    """
    import pandas as pd

    season_df = feedback_df[feedback_df["ScenarioType"].isin(season_scenarios)]
    grouped = season_df.groupby("user")["decision"].apply(lambda x: (x == "Valider").sum()).reset_index()
    grouped.columns = ["Utilisateur", "Score"]
    top_user = grouped.sort_values("Score", ascending=False).iloc[0]

    return {
        "🏆 Trophée de saison": "Champion communautaire",
        "Utilisateur": top_user["Utilisateur"],
        "Score": top_user["Score"]
    }
