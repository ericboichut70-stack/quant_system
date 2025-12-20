# 📦 Script release_packager.py — archivage de la version 1.0.0
import shutil
import os

def package_release(version="1.0.0", output_path="delivery/release_1.0.0.zip"):
    files = [
        "config/bot_release.yaml",
        "config/bot_changelog.yaml",
        "exports/bot_certificate.md",
        "exports/bot_release_notes.md",
        "exports/bot_metrics.csv",
        "exports/finalized_modules.md",
        "exports/mentor_validations.md"
    ]

    temp_dir = f"delivery/temp_release_{version.replace('.', '_')}"
    os.makedirs(temp_dir, exist_ok=True)

    for f in files:
        shutil.copy(f, os.path.join(temp_dir, os.path.basename(f)))

    shutil.make_archive(output_path.replace(".zip", ""), 'zip', temp_dir)
    shutil.rmtree(temp_dir)

    print(f"✅ release_{version}.zip généré dans {output_path}")

if __name__ == "__main__":
    package_release()
