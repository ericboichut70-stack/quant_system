# 🧩 Logique de progression collective
def compute_collective_progress(feedback_df, cross_df):
    """
    Calcule la progression collective de la communauté.
    """
    scenario_counts = feedback_df["ScenarioType"].value_counts().to_frame(name="Feedbacks")
    cross_counts = cross_df["scenario"].value_counts().to_frame(name="Validations croisées")

    progress_df = scenario_counts.join(cross_counts, how="outer").fillna(0)
    progress_df["Total validations"] = progress_df["Feedbacks"] + progress_df["Validations croisées"]
    return progress_df
