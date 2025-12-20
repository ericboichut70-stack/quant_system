# ❄️ Script bot_freezer.py — figer tous les fichiers liés à une version donnée
import shutil
import os

def freeze_bot(version="1.0.0", files=None, output_dir="delivery/frozen_bot"):
    if files is None:
        files = [
            "config/bot_manifest_final.yaml",
            "config/bot_release.yaml",
            "config/bot_changelog.yaml",
            "exports/bot_certificate.md",
            "exports/bot_release_notes.md",
            "exports/mentor_validations.md",
            "exports/finalized_modules.md"
        ]

    freeze_path = os.path.join(output_dir, f"v{version.replace('.', '_')}")
    os.makedirs(freeze_path, exist_ok=True)

    for f in files:
        shutil.copy(f, os.path.join(freeze_path, os.path.basename(f)))

    print(f"✅ Bot figé dans `{freeze_path}`")

if __name__ == "__main__":
    freeze_bot()
