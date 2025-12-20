# 📤 4. Export pédagogique
# 🎯 Objectif : Permettre à l’élève ou au mentor d’exporter :
# Journal pédagogique, Parcours scénarisé, Certification, Feedbacks reçus
def prepare_export(feedback_df, cross_df, coaching_df, user_name):
    """
    Prépare les données pédagogiques à exporter pour un élève.
    """
    import pandas as pd

    user_feedbacks = feedback_df[feedback_df["user"] == user_name]
    user_cross = cross_df[cross_df["user"] == user_name]
    user_coaching = coaching_df[coaching_df["user"] == user_name]

    export_df = pd.concat([
        user_feedbacks[["timestamp", "ScenarioType", "decision", "mentor"]],
        user_cross[["timestamp", "scenario", "decision", "validator"]],
        user_coaching[["timestamp", "recommendations"]]
    ], ignore_index=True).sort_values("timestamp")

    return export_df
