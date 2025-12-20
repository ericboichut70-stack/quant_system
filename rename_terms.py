# script de renommage
import os

def rename_terms(root_dir):
    replacements = {
        "Ballistic": "Ballistic",
        "ut_pivots": "ut_pivots",
        "phoebus_energy": "phoebus_energy"
    }

    for folder, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py") or file.endswith(".md"):
                path = os.path.join(folder, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                    for old, new in replacements.items():
                        content = content.replace(old, new)
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(content)
                except UnicodeDecodeError:
                    print(f"⚠️ Fichier ignoré (encodage non UTF-8) : {path}")

rename_terms(".")
