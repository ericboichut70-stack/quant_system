# ✅ Interface de transition vers la nouvelle saison
# 🎯 Objectif : Faciliter le passage d’une saison à la suivante en :
# Affichant le bilan de la saison écoulée, Proposant les premières quêtes ou défis de la nouvelle saison,
# Réinitialisant les compteurs ou rôles si nécessaire
def prepare_season_transition(old_season, new_season_name, new_scenarios, start_date, path="utils/season_transition_log.txt"):
    """
    Prépare la transition vers une nouvelle saison.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | Transition : {old_season['name']} → {new_season_name} | Scénarios : {', '.join(new_scenarios)} | Début : {start_date}\n")

    return {
        "Nouvelle saison": new_season_name,
        "Scénarios clés": new_scenarios,
        "Message": f"🌅 Nouvelle saison **{new_season_name}** lancée avec les scénarios : {', '.join(new_scenarios)}. Bonne exploration !"
    }
