# ✅ 5. Interface de binôme pédagogique
# 🎯 Objectif : Permettre à deux élèves de :
# Se lier en binôme, Suivre un parcours commun, Valider mutuellement leurs signaux, Recevoir un feedback croisé
def assign_binome(user1, user2, path="utils/binome_log.txt"):
    """
    Enregistre un binôme pédagogique.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {user1} | {user2}\n")

def load_binomes(path="utils/binome_log.txt"):
    """
    Charge les binômes enregistrés.
    """
    import pandas as pd
    return pd.read_csv(path, sep="|", names=["timestamp", "user1", "user2"])
