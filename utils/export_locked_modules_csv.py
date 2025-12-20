# 📤 Export .csv des modules verrouillés
import yaml
import csv

def export_locked_modules_csv(registry_path="config/module_registry.yaml", output_path="exports/locked_modules.csv"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Module", "Score", "Replay", "Export"])
        for name, data in registry.items():
            if data["status"] == "verrouillé":
                writer.writerow([name, data["score"], data["replay"], data["export"]])

    print("✅ locked_modules.csv généré.")

if __name__ == "__main__":
    export_locked_modules_csv()
