# ✅ Interface de classement saisonnier
# 🎯 Objectif : Permettre à la communauté de :
# Visualiser les scores individuels ou binômes sur une saison donnée,
# Comparer les contributions, Publier un classement saisonnier
def compute_seasonal_ranking(feedback_df, season_scenarios, season_name):
    """
    Calcule le classement saisonnier selon les scénarios clés.
    """
    import pandas as pd

    season_df = feedback_df[feedback_df["ScenarioType"].isin(season_scenarios)]
    grouped = season_df.groupby("user")["decision"].apply(lambda x: (x == "Valider").sum()).reset_index()
    grouped.columns = ["Utilisateur", f"Score ({season_name})"]
    return grouped.sort_values(f"Score ({season_name})", ascending=False)
