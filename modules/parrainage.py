# 🧑‍🤝‍🧑 Logique de parrainage entre élèves
def assign_parrain(user_name, parrain_name, path="utils/parrainage_log.txt"):
    """
    Enregistre une relation de parrainage entre deux utilisateurs.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {user_name} | {parrain_name}\n")


def load_parrainage(path="utils/parrainage_log.txt"):
    """
    Charge les relations de parrainage.
    """
    import pandas as pd
    return pd.read_csv(path, sep="|", names=["timestamp", "user", "parrain"])
