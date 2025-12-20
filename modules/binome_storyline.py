# 🧑‍🤝‍🧑 Logique de narration par binôme
# 🎯 Objectif : Permettre à chaque binôme de :
# Co-écrire une narration pédagogique, Relier leurs validations à des événements narratifs, Créer une mémoire binôme scénarisée
def record_binome_story(binome_members, title, scenario, outcome, path="utils/binome_story_log.txt"):
    """
    Enregistre un événement narratif lié à un binôme.
    """
    from datetime import datetime
    binome = " & ".join(binome_members)
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | Binôme : {binome} | {title} | Scénario : {scenario} | Issue : {outcome}\n")
