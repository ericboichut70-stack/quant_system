# run_all.py
# 🧩 Script d’orchestration
# Orchestration complète avec log : découpage → génération index → validation

import os

lot_dir = "../documentation_md/corpus_modulaire/lot_7"

def corriger_fichier(filepath):
    filename = os.path.basename(filepath)
    # Ne corriger que les variantes (_2, _3, etc.)
    if "_" in filename and filename.split("_")[-1].replace(".md", "").isdigit():
        with open(filepath, "r", encoding="utf-8") as f:
            contenu = f.read().strip()

        lignes = contenu.splitlines()
        modifie = False

        # Vérifier balise d'ouverture
        if not any(l.startswith("# === PROCLAMATION") for l in lignes):
            titre = filename.replace(".md", "").replace("_", " ").upper()
            en_tete = [
                f"# === PROCLAMATION {titre} ===",
                f"📜 Proclamation {titre}",
                f"### 📜 Proclamation {titre}",
                "@proclamation",
                "@ultime"
            ]
            lignes = en_tete + [""] + lignes
            modifie = True

        # Vérifier cachet de validation
        if not any(l.strip() == "# === FIN PROCLAMATION ===" for l in lignes):
            lignes.append("")
            lignes.append("# === FIN PROCLAMATION ===")
            modifie = True

        if modifie:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write("\n".join(lignes))
            print(f"Corrigé: {filepath}")
    else:
        print(f"Préservé (non variante): {filename}")

def corriger_lot(lot_dir):
    for fichier in os.listdir(lot_dir):
        if fichier.endswith(".md"):
            corriger_fichier(os.path.join(lot_dir, fichier))

if __name__ == "__main__":
    corriger_lot(lot_dir)
