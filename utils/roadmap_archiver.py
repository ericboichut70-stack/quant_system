# 📁 Script roadmap_archiver.py — déplacement vers l’historique
import yaml

def archive_roadmap(current_path="config/bot_roadmap.yaml", history_path="config/bot_roadmap_history.yaml"):
    with open(current_path, "r") as f:
        current = yaml.safe_load(f)

    try:
        with open(history_path, "r") as f:
            history = yaml.safe_load(f)
    except FileNotFoundError:
        history = []

    history.append({
        "version": current["next_version"],
        "date": current["planned_date"],
        "objectifs": current["objectifs"],
        "étapes": current["étapes"],
        "notes": current["notes"]
    })

    with open(history_path, "w") as f:
        yaml.dump(history, f)

    print("✅ Roadmap archivée dans `bot_roadmap_history.yaml`")

if __name__ == "__main__":
    archive_roadmap()
