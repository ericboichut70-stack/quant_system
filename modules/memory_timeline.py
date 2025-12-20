# Suivi de l’évolution des scores mémoire par scénario, dans le temps, à partir des feedbacks enregistrés.
import pandas as pd

def build_memory_timeline(feedback_df):
    """
    Construit une timeline d'évolution des scores mémoire par scénario.
    """
    feedback_df["timestamp"] = pd.to_datetime(feedback_df["timestamp"])
    feedback_df["score_change"] = feedback_df["decision"].map({"Valider": 1, "Rejeter": -1})
    
    timeline = (
        feedback_df.groupby(["ScenarioType", "timestamp"])
        .agg({"score_change": "sum"})
        .reset_index()
        .sort_values("timestamp")
    )

    timeline["cumulative_score"] = (
        timeline.groupby("ScenarioType")["score_change"]
        .cumsum()
    )

    return timeline
