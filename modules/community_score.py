# ✅ 1. Module de score communautaire
import pandas as pd

def compute_community_score(feedback_df):
    """
    Calcule un score communautaire pour chaque scénario.
    """
    score_df = (
        feedback_df[feedback_df["decision"] == "Valider"]
        .groupby("ScenarioType")
        .agg({"mentor": "count"})
        .rename(columns={"mentor": "CommunityScore"})
        .reset_index()
    )
    return score_df
