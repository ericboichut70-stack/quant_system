# 👥 Structure du bloc community_scoring + rôles multi-utilisateur
# Appel possible pour créer des profils, des rôles, ou des tableaux de progression.
# modules/community_scoring.py

def aggregate_scores(user_scores):
    """
    Agrège les scores d'une communauté d'utilisateurs.
    """
    total = sum(user_scores)
    count = len(user_scores)
    return round(total / count, 2) if count else 0

def assign_role(score):
    """
    Attribue un rôle selon le score moyen.
    """
    if score >= 90:
        return "🧠 Mentor"
    elif score >= 75:
        return "🎓 Validateur"
    elif score >= 60:
        return "📘 Apprenant"
    else:
        return "🔍 Observateur"
