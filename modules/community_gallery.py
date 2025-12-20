# ✅ Interface de galerie communautaire
# 🎯 Objectif : Permettre à la communauté de :
# Visualiser les badges, rôles et trophées obtenus par les membres,
# Filtrer par saison, binôme, ou type de récompense, Créer un espace de reconnaissance collective
def build_community_gallery(badge_log_path="utils/community_badge_log.txt"):
    """
    Construit la galerie communautaire à partir des badges enregistrés.
    """
    import pandas as pd
    try:
        gallery = pd.read_csv(badge_log_path, sep="|", names=["timestamp", "user", "badge", "saison"])
    except FileNotFoundError:
        gallery = pd.DataFrame(columns=["timestamp", "user", "badge", "saison"])
    return gallery.sort_values("timestamp", ascending=False)
