# ✅ Interface de défi inter-binôme
# 🎯 Objectif : Permettre à deux binômes de :
# Relever un défi pédagogique commun, Valider des scénarios imposés,
# Recevoir une récompense collective, Suivre leur progression comparative
def launch_interpair_challenge(binome1, binome2, scenario, goal, duration_days, path="utils/interpair_challenge_log.txt"):
    """
    Lance un défi inter-binôme.
    """
    from datetime import datetime, timedelta
    deadline = datetime.now() + timedelta(days=duration_days)
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {binome1} vs {binome2} | {scenario} | Objectif : {goal} | Deadline : {deadline.date()}\n")

def load_interpair_challenges(path="utils/interpair_challenge_log.txt"):
    """
    Charge les défis inter-binômes.
    """
    import pandas as pd
    return pd.read_csv(path, sep="|", names=["timestamp", "binomes", "scenario", "objectif", "deadline"])
