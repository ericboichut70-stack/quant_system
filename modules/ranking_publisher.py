# ✅ Interface de publication des classements
# 🎯 Objectif : Permettre aux mentors ou administrateurs de :
# Publier les classements des élèves, binômes ou groupes, Choisir le format (tournoi, score binôme, progression individuelle)
# Ajouter un commentaire ou un titre, Rendre le classement visible dans un espace communautaire
def publish_ranking(title, ranking_df, comment, path="utils/ranking_log.txt"):
    """
    Publie un classement pédagogique dans l’espace communautaire.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {title} | {comment}\n")
        for _, row in ranking_df.iterrows():
            f.write(f"{row.to_dict()}\n")

def load_published_rankings(path="utils/ranking_log.txt"):
    """
    Charge les classements publiés.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()
