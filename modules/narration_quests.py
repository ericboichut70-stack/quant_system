# 🧩 Amorçage du bloc narration_quests + rôles et badges
# Appel possible depuis l'interface ou test pour générer des quêtes et attribuer des badges.
# modules/narration_quests.py

def generate_quest(scenario_type, score):
    if score >= 80:
        return f"🎯 Quête : Exploiter le scénario '{scenario_type}' dans un contexte réel avec validation mentorale."
    elif score >= 60:
        return f"🧪 Quête : Simuler le scénario '{scenario_type}' avec feedback pédagogique."
    else:
        return f"🔍 Quête : Réviser le scénario '{scenario_type}' et proposer une amélioration."

def assign_badge(score):
    if score >= 90:
        return "🏅 Badge Or"
    elif score >= 75:
        return "🥈 Badge Argent"
    elif score >= 60:
        return "🥉 Badge Bronze"
    else:
        return "🔧 Badge Apprenti"
