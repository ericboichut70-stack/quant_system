# 📋 Export .md des versions planifiées
# --> Pour un export plus condensé, car déjà généré via le bouton # 🧭 “Générer synthèse 
# prévisionnelle” (bot_roadmap_forecast.md) dans bot_dashboard.py.
import yaml

def export_forecast_index_md(forecast_path="config/bot_roadmap_forecast.yaml", output_path="exports/bot_forecast_index.md"):
    with open(forecast_path, "r") as f:
        forecast = yaml.safe_load(f)

    lines = ["# 🧭 Index des versions planifiées\n\n",
             "| Version | Date prévue | Objectif principal |\n",
             "|---------|-------------|---------------------|\n"]

    for entry in forecast["versions"]:
        lines.append(f"| {entry['version']} | {entry['date']} | {entry['objectifs'][0]} |\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_forecast_index.md généré.")

if __name__ == "__main__":
    export_forecast_index_md()
