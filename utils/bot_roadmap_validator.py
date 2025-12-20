# ✅ Bloc bot_roadmap_validator.py — vérification de faisabilité
import yaml

def validate_forecast_goals(forecast_path="config/bot_roadmap_forecast.yaml", registry_path="config/module_registry.yaml"):
    with open(forecast_path, "r") as f:
        forecast = yaml.safe_load(f)
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    print("✅ Vérification de faisabilité des objectifs :\n")
    for entry in forecast["versions"]:
        print(f"🔮 Version {entry['version']} — {entry['date']}")
        for goal in entry["objectifs"]:
            keywords = goal.lower().split()
            match = any(k in registry for k in keywords)
            status = "🟢 Faisable" if match else "🔴 À structurer"
            print(f"- {goal} → {status}")
        print("—" * 40)

if __name__ == "__main__":
    validate_forecast_goals()
