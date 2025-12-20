# decoupage_proclamations.py
# 🧩 Script d’automatisation

import os
from datetime import datetime

source_file = "index_consolidated.md"
output_dir = "../documentation_md/corpus_modulaire"
os.makedirs(output_dir, exist_ok=True)

prefix_map = {
    "PROCLAMATION UNITAIRE": "01_proclamations_unitaire.md",
    "PROCLAMATION SINGULARITAIRE": "02_proclamations_singularitaire.md",
    "PROCLAMATION MONADIQUE": "03_proclamations_monadique.md",
    "PROCLAMATION ARCHÉTYPALE": "04_proclamations_archetypale.md",
    "PROCLAMATION PROTOTYPALE": "05_proclamations_prototypale.md",
    "PROCLAMATION PARADIGMATIQUE": "06_proclamations_paradigmatique.md",
    "PROCLAMATION AXIOLOGIQUE": "07_proclamations_axiologique.md",
    "PROCLAMATION MÉMORIALE": "08_proclamations_memoriale.md",
    "PROCLAMATION ARCHIVISTIQUE": "09_proclamations_archivistique.md",
    "PROCLAMATION CODICILLAIRE": "10_proclamations_codicillaire.md",
    "PROCLAMATION NOTARIÉE": "11_proclamations_notariee.md",
    "PROCLAMATION DIPLOMATIQUE": "12_proclamations_diplomatique.md",
    "PROCLAMATION CONSTITUTIONNELLE": "13_proclamations_constitutionnelle.md",
    "PROCLAMATION LÉGISLATIVE": "14_proclamations_legislative.md",
    "PROCLAMATION JUDICIAIRE": "15_proclamations_judiciaire.md",
    "PROCLAMATION EXÉGÉTIQUE": "16_proclamations_exegetique.md"
}

date_stamp = datetime.now().strftime("%d %B %Y")

with open(source_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

current_block = []
current_title = None

for line in lines:
    if line.startswith("# === PROCLAMATION"):
        current_title = line.strip().replace("# === ", "").replace(" ULTIME ===", "")
        current_block = []
        # Bandeau d’ouverture stylisé
        current_block.append(f"# 🏛️ {current_title} — Proclamation Ultime\n")
        current_block.append("---\n")
    elif line.startswith("# === FIN PROCLAMATION ==="):
        current_block.append(line)
        # Encadré visuel de traçabilité
        current_block.append("\n---\n")
        current_block.append(f"> 📍 Extrait de index_consolidated.md — découpé le {date_stamp}\n")
        current_block.append("> 🔏 Cachet : VALIDÉ — extrait du corpus consolidé\n")
        current_block.append("> ✍️ Signé : Eric\n")
        current_block.append("---\n")
        filename = prefix_map.get(current_title, f"{current_title.replace(' ', '_').lower()}.md")
        with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as out:
            out.writelines(current_block)
        current_block = []
        current_title = None
    elif current_title:
        current_block.append(line)
