# Validation ou rejet les demandes de réactivation
def load_reactivation_requests(path="utils/reactivation_requests.txt"):
    """
    Charge les demandes de réactivation en attente.
    """
    import pandas as pd
    df = pd.read_csv(path, sep="|", names=["timestamp", "scenario", "mentor", "comment"])
    return df


def approve_reactivation(scenario_name, memory_dict):
    """
    Valide la réactivation d’un scénario en le réinitialisant.
    """
    memory_dict[scenario_name] = max(0, memory_dict.get(scenario_name, 0))
    return memory_dict
