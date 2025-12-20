# 📤 Export .csv de bot_metrics.yaml
import yaml
import csv

def export_metrics_csv(metrics_path="config/bot_metrics.yaml", output_path="exports/bot_metrics.csv"):
    with open(metrics_path, "r") as f:
        metrics = yaml.safe_load(f)

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Métrique", "Valeur"])
        for key, value in metrics.items():
            writer.writerow([key, value])

    print("✅ bot_metrics.csv généré.")

if __name__ == "__main__":
    export_metrics_csv()
