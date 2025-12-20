# 🛠️ Script summary_updater.py — mise à jour automatique de
import yaml
from datetime import datetime

def update_summary(registry_path="config/module_registry.yaml", manifest_path="config/bot_manifest.yaml", output_path="exports/bot_summary.md"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    with open(manifest_path, "r") as f:
        manifest = yaml.safe_load(f)

    locked = {k: v for k, v in registry.items() if v["status"] == "verrouillé"}
    testing = {k: v for k, v in registry.items() if v["status"] == "actif"}

    lines = [
        "# 📘 Synthèse du bot — Private Assistant\n\n",
        "## Modules verrouillés\n"
    ]
    for name, data in locked.items():
        lines.append(f"- {name} (Score: {data['score']})\n")

    lines.append("\n## Modules en test\n")
    for name in testing:
        lines.append(f"- {name}\n")

    lines.append("\n## Fonctionnalités activées\n")
    for feature, active in manifest.get("features", {}).items():
        lines.append(f"- {feature.capitalize()} : {'✅' if active else '❌'}\n")

    lines.append(f"\n## Dernière activation\n- 📅 {datetime.now().strftime('%Y-%m-%d')}\n")
    lines.append(f"- 🧠 Mode : {manifest.get('mode', 'simulation')}\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_summary.md mis à jour.")

if __name__ == "__main__":
    update_summary()
