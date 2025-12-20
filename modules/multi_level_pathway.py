# ✅ Logique de progression scénarisée multi-niveaux
def assign_level(feedback_df, user_name, coherence_df):
    """
    Attribue un niveau pédagogique à un élève selon ses validations et sa cohérence.
    """
    user_df = feedback_df[feedback_df["user"] == user_name]
    valides = (user_df["decision"] == "Valider").sum()
    coherence = coherence_df.get("Cohérence (%)", {}).get(user_name, 100)

    if valides >= 30 and coherence >= 70:
        return "Avancé"
    elif valides >= 20 and coherence >= 60:
        return "Intermédiaire"
    else:
        return "Débutant"
