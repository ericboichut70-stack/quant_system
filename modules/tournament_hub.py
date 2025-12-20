# ✅ Interface de tournoi pédagogique
# 🎯 Objectif : Organiser un tournoi pédagogique entre élèves ou binômes :
# Scénarios imposés, Durée définie, Score calculé, Classement affiché
def launch_tournament(name, scenario_list, duration_days, path="utils/tournament_log.txt"):
    """
    Lance un tournoi pédagogique.
    """
    from datetime import datetime, timedelta
    deadline = datetime.now() + timedelta(days=duration_days)
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {name} | {','.join(scenario_list)} | {deadline.date()}\n")

def compute_tournament_scores(feedback_df, tournament_log):
    """
    Calcule les scores des participants à un tournoi.
    """
    import pandas as pd
    tournaments = pd.read_csv(tournament_log, sep="|", names=["timestamp", "name", "scenarios", "deadline"])
    scores = []

    for _, row in tournaments.iterrows():
        scenarios = row["scenarios"].split(",")
        participants = feedback_df[feedback_df["ScenarioType"].isin(scenarios)]
        grouped = participants.groupby("user")["decision"].apply(lambda x: (x == "Valider").sum())
        for user, score in grouped.items():
            scores.append({"Tournoi": row["name"], "Participant": user, "Score": score})

    return pd.DataFrame(scores).sort_values(["Tournoi", "Score"], ascending=[True, False])
