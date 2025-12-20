# 📋 Export .md de la feuille de route
import yaml

def export_roadmap_md(roadmap_path="config/bot_roadmap.yaml", output_path="exports/bot_roadmap.md"):
    with open(roadmap_path, "r") as f:
        roadmap = yaml.safe_load(f)

    lines = [f"# 🗺️ Feuille de route — Version {roadmap['next_version']}\n\n",
             f"**Date prévue** : {roadmap['planned_date']}\n\n",
             "## Objectifs\n"]
    for obj in roadmap["objectifs"]:
        lines.append(f"- {obj}\n")

    lines.append("\n## Étapes\n")
    for step in roadmap["étapes"]:
        status = "✅" if "[x]" in step else "⬜"
        label = step.replace("[x]", "").replace("[ ]", "").strip()
        lines.append(f"- {status} {label}\n")

    lines.append("\n## Notes\n")
    for note in roadmap["notes"]:
        lines.append(f"- {note}\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_roadmap.md généré.")

if __name__ == "__main__":
    export_roadmap_md()
