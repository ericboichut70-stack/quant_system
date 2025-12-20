# validate_extracted_files.py
# 🧩 Script de validation

import os

input_dir = "../documentation_md/corpus_modulaire/lot_1"

def validate_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    errors = []
    if "# === PROCLAMATION" not in content:
        errors.append("❌ Balise d’ouverture manquante")
    if "# === FIN PROCLAMATION ===" not in content:
        errors.append("❌ Balise de fermeture manquante")
    if "🔏 Cachet : VALIDÉ" not in content:
        errors.append("❌ Cachet de validation manquant")
    return errors

def main():
    all_files = [f for f in os.listdir(input_dir) if f.endswith(".md")]
    for file in sorted(all_files):
        filepath = os.path.join(input_dir, file)
        errors = validate_file(filepath)
        if errors:
            print(f"{file} → ERREURS détectées :")
            for e in errors:
                print("   ", e)
        else:
            print(f"{file} → ✅ Conforme")

if __name__ == "__main__":
    main()
