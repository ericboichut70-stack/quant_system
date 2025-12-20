# 🗜️ Générer un fichier .zip contenant tous les exports
# 📌 Résultat : export_all.zip dans exports/, contenant tous les .md, .yaml, .wav, .mp3
import zipfile
import os

def export_zip_all(zip_path="exports/export_all.zip"):
    folders = [
        "exports",
        "exports/audio",
        "config"
    ]
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for folder in folders:
            for root, _, files in os.walk(folder):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, start="exports")
                    zipf.write(full_path, arcname)
    print(f"✅ Archive ZIP générée : {zip_path}")
