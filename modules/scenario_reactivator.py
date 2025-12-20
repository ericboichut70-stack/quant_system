# Permet à l’utilisateur de réactiver manuellement un scénario désactivé
import pandas as pd

def reactivate_scenario(memory_dict, scenario_name):
    """
    Réactive manuellement un scénario en réinitialisant ou relevant son score mémoire.
    """
    if scenario_name not in memory_dict:
        memory_dict[scenario_name] = 0
    elif memory_dict[scenario_name] < 0:
        memory_dict[scenario_name] = 0
    return memory_dict


def save_memory_dict(memory_dict, path="utils/memory_state.csv"):
    """
    Sauvegarde le dictionnaire mémoire dans un fichier CSV.
    """
    df = pd.DataFrame(memory_dict.items(), columns=["ScenarioType", "Score"])
    df.to_csv(path, index=False)

# 🧑‍🏫 Validation mentorale avant réactivation
def request_mentor_validation(scenario_name, mentor_name, comment, path="utils/reactivation_requests.txt"):
    """
    Enregistre une demande de réactivation soumise au mentor.
    """
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {scenario_name} | {mentor_name} | {comment}\n")
