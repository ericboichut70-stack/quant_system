# ✅ Interface communautaire de publication et scoring croisé
# 🎯 Objectif : Permettre à chaque élève de : Publier ses signaux ou parcours,
# Recevoir des votes ou commentaires, Contribuer à un scoring communautaire
def publish_signal(user, scenario, score, comment, path="utils/community_log.txt"):
    """
    Publie un signal dans l’espace communautaire.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {user} | {scenario} | {score} | {comment}\n")

def load_community_signals(path="utils/community_log.txt"):
    """
    Charge les signaux publiés dans la communauté.
    """
    import pandas as pd
    return pd.read_csv(path, sep="|", names=["timestamp", "user", "scenario", "score", "comment"])
