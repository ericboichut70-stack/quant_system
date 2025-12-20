# ✅ Interface de galerie de badges
# 🎯 Objectif : Afficher tous les badges disponibles dans une galerie visuelle, avec :
# Icône, Nom, Description, Critère d’obtention
def get_badge_catalog():
    """
    Renvoie le catalogue complet des badges pédagogiques.
    """
    return [
        {"emoji": "🎓", "nom": "Validation Expert", "niveau": "Or", "description": "30 validations confirmées"},
        {"emoji": "🤝", "nom": "Binôme d’Or", "niveau": "Argent", "description": "Score binôme > 50"},
        {"emoji": "🏆", "nom": "Champion de Tournoi", "niveau": "Or", "description": "Score tournoi > 20"},
        {"emoji": "📈", "nom": "Progression Active", "niveau": "Bronze", "description": "10 validations sans badge majeur"}
    ]
