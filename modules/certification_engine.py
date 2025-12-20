# 🧩 Module de certification
import pandas as pd

def evaluate_certification(feedback_df, min_validations=50, min_ratio=0.75):
    """
    Évalue si un élève peut être certifié selon ses feedbacks.
    """
    stats = (
        feedback_df.groupby("user")
        .agg(total=("decision", "count"), valides=("decision", lambda x: (x == "Valider").sum()))
        .reset_index()
    )
    stats["ratio"] = stats["valides"] / stats["total"]
    stats["certified"] = (stats["valides"] >= min_validations) & (stats["ratio"] >= min_ratio)
    return stats
