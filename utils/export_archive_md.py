# 📋 Export .md de l’archive roadmap
import yaml

def export_archive_md(archive_path="config/bot_registry_archive.yaml", output_path="exports/bot_registry_archive.md"):
    with open(archive_path, "r") as f:
        archive = yaml.safe_load(f)

    lines = ["# 📦 Archive des artefacts livrés — Private Assistant\n\n"]
    for entry in archive:
        lines.append(f"## Version {entry['version']} — {entry['date']}\n")
        for art in entry["artefacts"]:
            lines.append(f"- {art}\n")
        lines.append("\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_registry_archive.md généré.")

if __name__ == "__main__":
    export_archive_md()
