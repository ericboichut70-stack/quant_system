# 🌍 Logique de saison communautaire
# 🎯 Objectif : Structurer la progression de toute la communauté en saisons thématiques :
# Chaque saison a ses scénarios, badges, défis; Les membres contribuent collectivement,
# Un classement ou une récompense communautaire est attribuée
def define_community_season(name, scenarios, start_date, end_date, path="utils/community_season_log.txt"):
    """
    Définit une saison communautaire.
    """
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{start_date} → {end_date} | {name} | Scénarios : {', '.join(scenarios)}\n")

def get_active_season(path="utils/community_season_log.txt"):
    """
    Récupère la saison communautaire active.
    """
    import pandas as pd
    seasons = pd.read_csv(path, sep="|", names=["dates", "name", "scenarios"])
    return seasons.tail(1).to_dict(orient="records")[0]
