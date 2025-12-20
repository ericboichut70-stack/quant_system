# 📋 2. Export .md des signatures
import yaml

def export_signatures_md(signatures_path="config/bot_roadmap_signatures.yaml", output_path="exports/bot_roadmap_signatures.md"):
    with open(signatures_path, "r") as f:
        signatures = yaml.safe_load(f)

    lines = ["# ✍️ Signatures roadmap — Private Assistant\n\n"]
    for version, data in signatures.items():
        lines.append(f"## Version {version}\n")
        lines.append("### Mentors :\n")
        for mentor in data.get("mentor", []):
            lines.append(f"- {mentor['nom']} ({mentor['rôle']}) — Score : {mentor['score']}\n")
            lines.append(f"  > {mentor['commentaire']}\n")
        lines.append("### Communautaire :\n")
        for entry in data.get("communautaire", []):
            for k, v in entry.items():
                lines.append(f"- {k} : {v}\n")
        lines.append("\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_roadmap_signatures.md généré.")

if __name__ == "__main__":
    export_signatures_md()
