# 🧪 Bloc bot_roadmap_simulator.py — test des étapes futures
import yaml

def simulate_roadmap_steps(forecast_path="config/bot_roadmap_forecast.yaml"):
    with open(forecast_path, "r") as f:
        forecast = yaml.safe_load(f)

    print("🧪 Simulation des étapes futures :\n")
    for entry in forecast["versions"]:
        print(f"🔮 Version {entry['version']} — {entry['date']}")
        for goal in entry["objectifs"]:
            print(f"✅ Étape simulée : {goal}")
        print("—" * 40)

if __name__ == "__main__":
    simulate_roadmap_steps()
