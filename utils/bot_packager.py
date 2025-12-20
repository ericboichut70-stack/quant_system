# 📦 Script bot_packager.py — archivage des fichiers de production
import shutil
import os

def package_bot(source_dirs=None, output_path="delivery/bot_package.zip"):
    if source_dirs is None:
        source_dirs = ["config", "exports", "replays", "interface_pilotage", "utils"]

    temp_dir = "delivery/temp_package"
    os.makedirs(temp_dir, exist_ok=True)

    for d in source_dirs:
        shutil.copytree(d, os.path.join(temp_dir, d), dirs_exist_ok=True)

    shutil.make_archive(output_path.replace(".zip", ""), 'zip', temp_dir)
    shutil.rmtree(temp_dir)

    print(f"✅ bot_package.zip généré dans {output_path}")

if __name__ == "__main__":
    package_bot()
