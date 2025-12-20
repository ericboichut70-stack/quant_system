# 📁 Module statistiques pédagogiques
import pandas as pd

def compute_feedback_stats(feedback_df, mode="global"):
    """
    Calcule les statistiques de feedback selon le mode choisi.
    Modes : 'global', 'scenario', 'mentor', 'decision'
    """
    if mode == "global":
        total = len(feedback_df)
        valides = (feedback_df["decision"] == "Valider").sum()
        rejetés = (feedback_df["decision"] == "Rejeter").sum()
        return pd.DataFrame({
            "Total": [total],
            "Validés": [valides],
            "Rejetés": [rejetés],
            "Taux validation (%)": [round(valides / total * 100, 2) if total else 0]
        })

    elif mode == "scenario":
        return feedback_df.groupby("ScenarioType")["decision"].value_counts().unstack().fillna(0)

    elif mode == "mentor":
        return feedback_df.groupby("mentor")["decision"].value_counts().unstack().fillna(0)

    elif mode == "decision":
        return feedback_df["decision"].value_counts().to_frame(name="Nombre")

    else:
        return compute_feedback_stats(feedback_df, mode="global")
