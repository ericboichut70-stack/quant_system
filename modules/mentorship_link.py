# ✅ Logique de parrainage mentoré
# 🎯 Objectif : Permettre à un mentoré de :
# Choisir un parrain, Recevoir des validations croisées, Progresser avec un binôme mentoré
def assign_mentor(user_name, mentor_name, path="utils/mentorship_log.txt"):
    """
    Crée un lien de parrainage mentoré.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {user_name} | Parrain : {mentor_name}\n")

def load_mentorships(path="utils/mentorship_log.txt"):
    """
    Charge les liens de parrainage.
    """
    import pandas as pd
    return pd.read_csv(path, sep="|", names=["timestamp", "user", "mentor"])
