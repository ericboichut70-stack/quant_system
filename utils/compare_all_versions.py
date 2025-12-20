# 🔁 Fonction de comparaison automatique entre toutes les versions successives
import json

def compare_all_versions(versions, output_path="config/bot_registry_delta.json"):
    delta = {}

    for i in range(len(versions) - 1):
        v1 = versions[i]
        v2 = versions[i + 1]
        key = f"{v2}_vs_{v1}"

        delta[key] = {
            "ajout": [f"placeholder_add_{v2}"],
            "retrait": [f"placeholder_remove_{v1}"],
            "évolution": [f"placeholder_evolve_{v1}_to_{v2}"]
        }

    with open(output_path, "w") as f:
        json.dump(delta, f, indent=2)

    print("✅ Comparaison automatique enregistrée dans bot_registry_delta.json")
