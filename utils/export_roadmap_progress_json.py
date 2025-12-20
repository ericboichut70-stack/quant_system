# 📤 Export .json du tracker de progression
import yaml
import json

def export_roadmap_progress_json(roadmap_path="config/bot_roadmap.yaml", output_path="exports/bot_roadmap_progress.json"):
    with open(roadmap_path, "r") as f:
        roadmap = yaml.safe_load(f)

    progress = {
        "version": roadmap["next_version"],
        "planned_date": roadmap["planned_date"],
        "objectifs": roadmap["objectifs"],
        "étapes": [],
        "notes": roadmap["notes"]
    }

    for step in roadmap["étapes"]:
        label = step.replace("[x]", "").replace("[ ]", "").strip()
        done = "[x]" in step
        progress["étapes"].append({"étape": label, "réalisée": done})

    with open(output_path, "w") as f:
        json.dump(progress, f, indent=2)

    print("✅ bot_roadmap_progress.json généré.")

if __name__ == "__main__":
    export_roadmap_progress_json()
