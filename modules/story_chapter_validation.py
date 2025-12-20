# ✅ Interface de chapitre validé
# 🎯 Objectif : Permettre à la communauté de :
# Proposer des chapitres narratifs, Valider collectivement ceux qui deviennent “canoniques”,
# Créer une trame évolutive et mémorable
def propose_chapter(user_name, title, content, path="utils/story_chapters_proposed.txt"):
    """
    Propose un chapitre narratif.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {user_name} | {title} | {content}\n")

def validate_chapter(title, validator_name, path="utils/story_chapters_validated.txt"):
    """
    Valide un chapitre proposé.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | Validé par : {validator_name} | {title}\n")
