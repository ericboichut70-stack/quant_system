# generate_annexes.py

import os
from datetime import datetime

output_dir = "corpus_modulaire"
os.makedirs(output_dir, exist_ok=True)

date_stamp = datetime.now().strftime("%d %B %Y")

# Liste des annexes à générer automatiquement
annexes = {
    "colophon.md": [
        "# 📜 Colophon\n",
        "---\n",
        f"Document généré et découpé le {date_stamp}\n",
        "Ce colophon décrit l’origine, la méthode et la finalité du corpus.\n",
        "---\n"
    ],
    "reliquaire.md": [
        "# 🗝️ Reliquaire\n",
        "---\n",
        "Ce reliquaire conserve les fragments ultimes et les traces mémorielles du corpus.\n",
        "---\n"
    ],
    "registre_final.md": [
        "# 📖 Registre Final\n",
        "---\n",
        "Ce registre consigne la clôture définitive du cycle, avec validation et transmission.\n",
        "---\n"
    ],
    "banner_annexes.md": [
        "# 🎌 Bannière des Annexes Finales\n",
        "---\n",
        "Cette bannière marque l’ouverture des annexes et leur intégration au corpus.\n",
        "---\n"
    ]
}

def main():
    for fname, content in annexes.items():
        path = os.path.join(output_dir, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(content)
    print("✅ Annexes générées et placées dans corpus_modulaire/")

if __name__ == "__main__":
    main()
