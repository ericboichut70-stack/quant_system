# 📈 Structure du bloc progression_tracker.py
# Possible de l’utiliser pour suivre les étapes : "non commencé", "en cours", "validé", "rejoué", etc.
# modules/progression_tracker.py

def update_progression(user_progress, scenario, status):
    """
    Met à jour l'état d'avancement d'un scénario pour un utilisateur.
    """
    user_progress[scenario] = status
    return user_progress

def summarize_progression(user_progress):
    """
    Résume les étapes franchies.
    """
    summary = []
    for scenario, status in user_progress.items():
        summary.append(f"{scenario} → {status}")
    return summary
