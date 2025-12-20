# 📘 Export .md de bot_registry_scripts.yaml pour documentation externe
import yaml

def export_scripts_md(script_path="config/bot_registry_scripts.yaml", output_path="exports/bot_registry_scripts.md"):
    with open(script_path, "r") as f:
        scripts = yaml.safe_load(f)

    lines = ["# 🧭 Index des scripts utilitaires — Private Assistant\n\n"]
    for name, meta in scripts.items():
        lines.append(f"## {name}\n")
        lines.append(f"- Rôle : {meta['rôle']}\n")
        lines.append(f"- Génère : {meta['génère']}\n")
        lines.append(f"- Source : {meta['source']}\n\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_registry_scripts.md généré.")
