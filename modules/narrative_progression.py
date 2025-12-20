# 📖 2. Interface de progression narrative
# 🎯 Objectif : Offrir à l’élève une narration immersive de sa progression :
# Étapes franchies, Défis relevés, Récompenses obtenues, Prochaines missions
def generate_narrative(feedback_df, rewards, user_name):
    """
    Génère une narration pédagogique pour un élève.
    """
    valides = feedback_df[(feedback_df["user"] == user_name) & (feedback_df["decision"] == "Valider")].shape[0]

    story = [f"🧠 {user_name}, ton aventure pédagogique progresse avec {valides} validations à ton actif."]

    if "🎓 Badge 'Validation Expert'" in rewards:
        story.append("🎓 Tu as atteint le rang de 'Validation Expert'. Tes signaux sont précis et réguliers.")
    if "🤝 Badge 'Binôme d’Or'" in rewards:
        story.append("🤝 Ton binôme est reconnu pour sa cohérence et son engagement mutuel.")
    if "🏆 Badge 'Champion de Tournoi'" in rewards:
        story.append("🏆 Tu as brillé en tournoi, prouvant ta maîtrise dans un cadre compétitif.")
    if "📈 Badge 'Progression Active'" in rewards:
        story.append("📈 Tu avances avec constance. Continue à explorer de nouveaux scénarios.")

    story.append("🚀 Prochaine étape : tester un scénario avancé ou relever un défi mentoré.")

    return "\n".join(story)
 