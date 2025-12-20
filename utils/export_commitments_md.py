# 📋 Export .md des engagements roadmap
import yaml

def export_commitments_md(commitments_path="config/bot_roadmap_commitments.yaml", output_path="exports/bot_roadmap_commitments.md"):
    with open(commitments_path, "r") as f:
        commitments = yaml.safe_load(f)

    lines = ["# 📜 Engagements roadmap — Private Assistant\n\n"]
    for version, data in commitments.items():
        lines.append(f"## Version {version}\n")
        lines.append(f"- Certifié : {data['certifié']}\n")
        lines.append(f"- Livré : {data['livré']}\n")
        lines.append("### Engagements :\n")
        for item in data["engagements"]:
            lines.append(f"- {item}\n")
        lines.append("\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_roadmap_commitments.md généré.")

if __name__ == "__main__":
    export_commitments_md()
