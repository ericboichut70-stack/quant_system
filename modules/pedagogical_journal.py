# 📘 Module de journal pédagogique
def build_pedagogical_journal(feedback_df, cross_df, coaching_df, pause_log, user_name):
    """
    Construit le journal pédagogique complet d’un élève.
    """
    import pandas as pd

    user_feedbacks = feedback_df[feedback_df["user"] == user_name]
    user_cross = cross_df[cross_df["user"] == user_name]
    user_coaching = coaching_df[coaching_df["user"] == user_name]
    user_pause = pause_log[pause_log["user"] == user_name]

    journal = pd.concat([
        user_feedbacks[["timestamp", "ScenarioType", "decision", "mentor"]],
        user_cross[["timestamp", "scenario", "decision", "validator"]],
        user_coaching[["timestamp", "recommendations"]],
        user_pause[["timestamp", "status"]]
    ], ignore_index=True).sort_values("timestamp")

    return journal
