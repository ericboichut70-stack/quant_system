# 📋 Création d'un export .md de bot_registry_map.yaml pour documentation externe
import yaml

def export_map_md(map_path="config/bot_registry_map.yaml", output_path="exports/bot_registry_map.md"):
    with open(map_path, "r") as f:
        map_data = yaml.safe_load(f)

    lines = ["# 🗺️ Cartographie des artefacts — Private Assistant\n\n"]
    for file, content in map_data.items():
        lines.append(f"## {file}\n")
        for key, items in content.items():
            lines.append(f"### {key.capitalize()} :\n")
            for item in items:
                lines.append(f"- {item}\n")
        lines.append("\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_registry_map.md généré.")
