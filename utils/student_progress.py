# 📁 Tableau de progression élève
import pandas as pd

def build_student_progress(feedback_df, user_name):
    """
    Construit le tableau de progression pédagogique pour un élève.
    """
    user_df = feedback_df[feedback_df["user"] == user_name]
    total = len(user_df)
    valides = (user_df["decision"] == "Valider").sum()
    ratio = round(valides / total * 100, 2) if total else 0

    scenario_stats = user_df["ScenarioType"].value_counts().to_frame(name="Occurrences")
    scenario_validations = (
        user_df[user_df["decision"] == "Valider"]["ScenarioType"]
        .value_counts()
        .to_frame(name="Validations")
    )

    progress_df = scenario_stats.join(scenario_validations, how="left").fillna(0)
    return total, valides, ratio, progress_df
