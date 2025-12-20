# 🧠 Module de mémoire évolutive

def update_memory_from_feedback(memory_dict, feedback_df):
    """
    Met à jour la mémoire pédagogique selon les feedbacks mentoraux.
    """
    for _, row in feedback_df.iterrows():
        scenario = row.get("ScenarioType")
        decision = row.get("decision")

        if not scenario or not decision:
            continue

        if decision == "Rejeter":
            memory_dict[scenario] = memory_dict.get(scenario, 0) - 1
        elif decision == "Valider":
            memory_dict[scenario] = memory_dict.get(scenario, 0) + 1

    return memory_dict


def apply_memory_to_score(base_score, scenario, memory_dict):
    """
    Ajuste le score de confiance selon la mémoire pédagogique.
    """
    adjustment = memory_dict.get(scenario, 0)
    return max(0, min(10, base_score + adjustment))


def filter_scenarios_by_memory(memory_dict, threshold=-2):
    """
    Filtre les scénarios à proposer selon leur score mémoire.
    """
    return [s for s, score in memory_dict.items() if score > threshold]


def suggest_adjustments_from_memory(memory_dict):
    """
    Génère des suggestions pédagogiques ciblées selon la mémoire.
    """
    suggestions = []
    for scenario, score in memory_dict.items():
        if score < -2:
            suggestions.append(f"⚠️ Le scénario '{scenario}' est souvent rejeté. À revoir ou désactiver.")
        elif score > 2:
            suggestions.append(f"✅ Le scénario '{scenario}' est validé régulièrement. À privilégier.")
    return suggestions

# 🔧 Mise à jour centralisée
def save_memory_state(memory_dict, path="utils/memory_state.csv"):
    """
    Sauvegarde le dictionnaire mémoire dans un fichier CSV central.
    """
    import pandas as pd
    from datetime import datetime

    df = pd.DataFrame([
        {"ScenarioType": s, "Score": score, "LastUpdated": datetime.today().strftime("%Y-%m-%d"), "IsActive": score >= -2}
        for s, score in memory_dict.items()
    ])
    df.to_csv(path, index=False)

# modules/memory_evolution.py

def apply_memory_to_score(score, scenario_type, memory_dict):
    memory_boost = memory_dict.get(scenario_type, 0)
    adjusted = score + memory_boost
    return min(adjusted, 100)
# Exemple d'appel du bloc memory_evolution.py:
# memory_dict = {"breaker": 5, "sweep": -3}
# adjusted_score = apply_memory_to_score(72, "sweep", memory_dict)
