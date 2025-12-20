# ✅ Interface de validation croisée mentor-parrain
# 🎯 Objectif : Permettre à un mentor ou parrain de :
# Valider les signaux d’un filleul, Ajouter un commentaire, Enregistrer la validation croisée
def cross_validate_signal(mentor_name, user_name, scenario, decision, comment, path="utils/cross_validation_log.txt"):
    """
    Enregistre une validation croisée mentor-parrain.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {mentor_name} → {user_name} | {scenario} | {decision} | {comment}\n")
