# ✅ 1. Module de scoring binôme
# 🎯 Objectif : Attribuer à chaque binôme un score pédagogique partagé, basé sur :
# Validations croisées, Cohérence entre les deux membres, Progression synchronisée, Engagement mutuel
def compute_binome_score(feedback_df, binome_log, memory_dict):
    """
    Calcule un score pédagogique pour chaque binôme.
    """
    import pandas as pd

    binomes = pd.read_csv(binome_log, sep="|", names=["timestamp", "user1", "user2"])
    scores = []

    for _, row in binomes.iterrows():
        u1, u2 = row["user1"], row["user2"]
        df_u1 = feedback_df[feedback_df["user"] == u1]
        df_u2 = feedback_df[feedback_df["user"] == u2]

        val_u1 = (df_u1["decision"] == "Valider").sum()
        val_u2 = (df_u2["decision"] == "Valider").sum()

        shared_scenarios = set(df_u1["ScenarioType"]) & set(df_u2["ScenarioType"])
        shared_score = sum([memory_dict.get(s, 0) for s in shared_scenarios])

        score = round((val_u1 + val_u2) * (shared_score / max(len(shared_scenarios), 1)), 2)
        scores.append({"Binôme": f"{u1} & {u2}", "Score binôme": score})

    return pd.DataFrame(scores).sort_values("Score binôme", ascending=False)
