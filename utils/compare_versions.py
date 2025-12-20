# ✅ “Comparer deux versions”
import json

def compare_versions(v1, v2, output_path="config/bot_registry_delta.json"):
    delta = {
        f"{v1}_vs_{v2}": {
            "ajout": ["placeholder_module"],
            "retrait": [],
            "évolution": ["placeholder_evolution"]
        }
    }

    try:
        with open(output_path, "r") as f:
            existing = json.load(f)
    except FileNotFoundError:
        existing = {}

    existing.update(delta)

    with open(output_path, "w") as f:
        json.dump(existing, f, indent=2)

    print(f"✅ Diff {v1} vs {v2} ajouté à bot_registry_delta.json")
