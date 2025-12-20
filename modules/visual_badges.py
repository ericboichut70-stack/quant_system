# ✅ Module de badge visuel
# 🎯 Objectif : Associer à chaque récompense pédagogique un badge visuel :
# Icône ou emoji, Couleur ou style, Description courte, Niveau (bronze, argent, or…)
def get_visual_badges(rewards):
    """
    Associe à chaque récompense un badge visuel.
    """
    badge_map = {
        "🎓 Badge 'Validation Expert'": {"emoji": "🎓", "color": "gold", "level": "Or"},
        "🤝 Badge 'Binôme d’Or'": {"emoji": "🤝", "color": "silver", "level": "Argent"},
        "🏆 Badge 'Champion de Tournoi'": {"emoji": "🏆", "color": "gold", "level": "Or"},
        "📈 Badge 'Progression Active'": {"emoji": "📈", "color": "bronze", "level": "Bronze"}
    }

    visual_badges = []
    for r in rewards:
        badge = badge_map.get(r)
        if badge:
            visual_badges.append({
                "Récompense": r,
                "Emoji": badge["emoji"],
                "Niveau": badge["level"],
                "Couleur": badge["color"]
            })

    return visual_badges
