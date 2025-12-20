# ✅ Module de cohérence mentor/parrain/bot
import pandas as pd

def compute_coherence(feedback_df, cross_df, auto_df):
    """
    Calcule la cohérence entre mentor, parrain et bot pour chaque scénario.
    """
    mentor_decisions = feedback_df.groupby("ScenarioType")["decision"].value_counts().unstack().fillna(0)
    parrain_decisions = cross_df.groupby("scenario")["decision"].value_counts().unstack().fillna(0)
    bot_decisions = auto_df.groupby("ScenarioType")["AutoDecision"].value_counts().unstack().fillna(0)

    combined = mentor_decisions.add(parrain_decisions, fill_value=0).add(bot_decisions, fill_value=0)
    combined["Total"] = combined.sum(axis=1)

    # Cohérence = % de décisions majoritaires alignées
    def majority_agreement(row):
        top = row.drop("Total").idxmax()
        count = row[top]
        return round(count / row["Total"] * 100, 2) if row["Total"] else 0

    combined["Cohérence (%)"] = combined.apply(majority_agreement, axis=1)
    return combined.sort_values("Cohérence (%)", ascending=False)
