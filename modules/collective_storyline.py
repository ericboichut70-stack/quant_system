# 🎬 Logique de scénarisation collective
# 🎯 Objectif : Permettre à la communauté de :
# Co-écrire une narration pédagogique, Proposer des événements, défis, rebondissements; Voter ou valider les chapitres
def propose_story_event(user_name, title, description, path="utils/storyline_log.txt"):
    """
    Propose un événement scénarisé collectif.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {user_name} | {title} | {description}\n")

def load_storyline(path="utils/storyline_log.txt"):
    """
    Charge la narration collective.
    """
    import pandas as pd
    return pd.read_csv(path, sep="|", names=["timestamp", "user", "title", "description"])
