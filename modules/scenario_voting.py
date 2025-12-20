# 🗳️ Logique de vote communautaire pour les scénarios
# 🎯 Objectif : Permettre à la communauté de :
# Proposer des scénarios pour la prochaine saison, Voter pour leurs préférés, Sélectionner les scénarios les plus plébiscités
def record_vote(user_name, scenario, path="utils/scenario_votes.txt"):
    """
    Enregistre un vote pour un scénario.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {user_name} | {scenario}\n")

def tally_votes(path="utils/scenario_votes.txt"):
    """
    Compte les votes par scénario.
    """
    import pandas as pd
    votes = pd.read_csv(path, sep="|", names=["timestamp", "user", "scenario"])
    tally = votes["scenario"].value_counts().reset_index()
    tally.columns = ["Scénario", "Votes"]
    return tally
