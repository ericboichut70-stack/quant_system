# 🧠 Structuration du bloc auto_mentor_feedback + validations
# Appel possible dans interface Streamlit ou CLI pour pré-valider les signaux.
# modules/auto_mentor_feedback.py

def auto_mentor_feedback(row):
    score = row["ConfidenceScore"]
    structure = row["ScenarioType"]

    if score >= 80:
        decision = "Valider"
        comment = f"Structure {structure} bien formée, score élevé"
    elif score >= 60:
        decision = "À revoir"
        comment = f"Structure {structure} correcte mais score moyen"
    else:
        decision = "Rejeter"
        comment = f"Structure {structure} faible, score insuffisant"

    return decision, comment
