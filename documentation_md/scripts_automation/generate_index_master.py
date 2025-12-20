# generate_index_master.py
# 📑 Script miroir — Génération automatique de 00_index_master.md

import os

DOSSIER = "../corpus_modulaire"
FICHIER_INDEX = "../00_index_master.md"

def main():
    fichiers = [f for f in os.listdir(DOSSIER) if f.endswith(".md")]
    fichiers.sort()  # tri alphabétique, donc 01, 02, etc.

    lignes = []
    lignes.append("# 📚 Index Maître du Corpus\n\n")
    lignes.append("## Proclamations\n")

    for f in fichiers:
        lignes.append(f"- [{f}](corpus_modulaire/{f})\n")

    lignes.append("\n## Annexes\n\n")
    lignes.append("## Archives\n")
    lignes.append("- [execution_log.txt](scripts_automation/execution_log.txt)\n\n")
    lignes.append("## Documentation\n")
    lignes.append("- [index_consolidated.md](scripts_automation/index_consolidated.md)\n")

    with open(FICHIER_INDEX, "w", encoding="utf-8") as out:
        out.writelines(lignes)

    print(f"✅ Index maître généré avec {len(fichiers)} proclamations.")

if __name__ == "__main__":
    main()
