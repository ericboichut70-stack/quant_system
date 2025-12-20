# 📤 Export .csv des modules en test et verrouillés
import yaml
import csv

def export_module_status_csv(registry_path="config/module_registry.yaml", output_path="exports/module_status.csv"):
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Module", "Status", "Score", "Replay", "Export"])
        for name, data in registry.items():
            writer.writerow([name, data["status"], data["score"], data["replay"], data["export"]])

    print("✅ module_status.csv généré.")

if __name__ == "__main__":
    export_module_status_csv()
