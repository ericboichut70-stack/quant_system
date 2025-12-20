# 📦 Script forecast_packager.py — archivage des versions à venir
import shutil
import os

def package_forecast(files=None, output_path="delivery/forecast_package.zip"):
    if files is None:
        files = [
            "config/bot_roadmap_forecast.yaml",
            "exports/bot_roadmap_forecast.md",
            "exports/bot_forecast_index.md"
        ]

    temp_dir = "delivery/temp_forecast"
    os.makedirs(temp_dir, exist_ok=True)

    for f in files:
        shutil.copy(f, os.path.join(temp_dir, os.path.basename(f)))

    shutil.make_archive(output_path.replace(".zip", ""), 'zip', temp_dir)
    shutil.rmtree(temp_dir)

    print(f"✅ forecast_package.zip généré dans {output_path}")

if __name__ == "__main__":
    package_forecast()
