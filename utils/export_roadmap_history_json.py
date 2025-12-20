# 📤 Export .json de l’historique roadmap
import yaml
import json

def export_roadmap_history_json(history_path="config/bot_roadmap_history.yaml", output_path="exports/bot_roadmap_history.json"):
    with open(history_path, "r") as f:
        history = yaml.safe_load(f)

    with open(output_path, "w") as f:
        json.dump(history, f, indent=2)

    print("✅ bot_roadmap_history.json généré.")

if __name__ == "__main__":
    export_roadmap_history_json()
