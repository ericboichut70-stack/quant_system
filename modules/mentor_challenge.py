# ✅ Module de défi mentoré
# 🎯 Objectif : Permettre à un mentor de lancer un défi pédagogique à un ou plusieurs élèves :
# Scénario imposé, Objectif de validation, Durée limitée, Suivi des résultats
def launch_mentor_challenge(mentor, scenario, goal, duration_days, path="utils/challenge_log.txt"):
    """
    Lance un défi mentoré.
    """
    from datetime import datetime, timedelta
    deadline = datetime.now() + timedelta(days=duration_days)
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {mentor} | {scenario} | {goal} | {deadline.date()}\n")

def load_challenges(path="utils/challenge_log.txt"):
    """
    Charge les défis mentorés.
    """
    import pandas as pd
    return pd.read_csv(path, sep="|", names=["timestamp", "mentor", "scenario", "goal", "deadline"])
