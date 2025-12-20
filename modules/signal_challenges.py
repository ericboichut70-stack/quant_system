# 🎮 Structure du bloc signal_challenges + niveaux de progression
# Appel possible pour générer des défis personnalisés selon le score ou le rôle.
# modules/signal_challenges.py

def generate_challenge(scenario, level):
    if level == "débutant":
        return f"🔰 Identifier un signal '{scenario}' sur un graphique statique."
    elif level == "intermédiaire":
        return f"⚔️ Simuler une entrée '{scenario}' avec TP/SL et justification."
    elif level == "avancé":
        return f"🏁 Valider un signal '{scenario}' en conditions réelles avec replay et scoring."
    else:
        return f"❓ Niveau inconnu pour '{scenario}'"

def assign_level(score):
    if score >= 90:
        return "avancé"
    elif score >= 70:
        return "intermédiaire"
    else:
        return "débutant"
