# 🧩 Module de validation croisée
def submit_cross_validation(scenario, validator, user, decision, comment, path="utils/cross_validation_log.txt"):
    """
    Enregistre une validation croisée entre utilisateurs.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {scenario} | {validator} | {user} | {decision} | {comment}\n")


def load_cross_validations(path="utils/cross_validation_log.txt"):
    """
    Charge les validations croisées enregistrées.
    """
    import pandas as pd
    return pd.read_csv(path, sep="|", names=["timestamp", "scenario", "validator", "user", "decision", "comment"])
