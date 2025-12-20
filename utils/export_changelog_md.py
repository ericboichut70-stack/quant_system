# 📋 Export .md du changelog technique
import yaml

def export_changelog_md(changelog_path="config/bot_changelog.yaml", output_path="exports/bot_changelog.md"):
    with open(changelog_path, "r") as f:
        changelog = yaml.safe_load(f)

    lines = ["# 🧮 Changelog technique — Private Assistant\n\n"]
    for entry in changelog:
        lines.append(f"## Version {entry['version']} — {entry['date']}\n")
        for commit in entry["commits"]:
            lines.append(f"- {commit}\n")
        lines.append("\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_changelog.md généré.")

if __name__ == "__main__":
    export_changelog_md()
