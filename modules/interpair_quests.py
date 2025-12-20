# ✅ Logique de quêtes inter-binômes
#🎯 Objectif : Proposer des quêtes collaboratives à deux binômes :
# Objectif commun, Validation croisée, Récompense partagée
def generate_interpair_quest(binome1, binome2, feedback_df):
    """
    Génère une quête inter-binôme.
    """
    all_users = binome1 + binome2
    df = feedback_df[feedback_df["user"].isin(all_users)]
    shared_scenarios = df["ScenarioType"].value_counts().head(1).index.tolist()

    quest = {
        "Binômes": [binome1, binome2],
        "Objectif": f"Valider 10 signaux sur le scénario '{shared_scenarios[0]}'",
        "Récompense": "🏆 Badge 'Synergie Binôme'"
    }

    return quest
