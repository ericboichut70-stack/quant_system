# ✅ Logique de relance communautaire
# 🎯 Objectif : Relancer l’engagement communautaire en :
# Identifiant les membres inactifs, Proposant des quêtes ou défis ciblés, Affichant des messages de relance personnalisés
def generate_reactivation_messages(feedback_df, user_list, threshold=3):
    """
    Génère des messages de relance pour les membres peu actifs.
    """
    messages = []
    for user in user_list:
        valides = (feedback_df[(feedback_df["user"] == user)]["decision"] == "Valider").sum()
        if valides < threshold:
            messages.append(f"👋 {user}, ta saison t’attend ! Rejoins une quête ou un binôme pour relancer ton aventure.")
    return messages
