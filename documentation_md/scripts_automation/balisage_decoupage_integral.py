# balisage_decoupage_integral.py
# Correctif avec balisage et découpage intégral

import os
import re
import unicodedata

SOURCE = "index_consolidated.md"
OUTPUT_DIR = "../corpus_modulaire"  # sortie sous documentation_md/corpus_modulaire
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Normalisation: retire accents, met en majuscules, simplifie espaces
def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.upper().strip()
    s = re.sub(r"\s+", " ", s)
    return s

# Cartographie des 16 proclamations principales → nom de fichier
PREFIX_MAP = {
    "PROCLAMATION UNITAIRE": "01_proclamations_unitaire.md",
    "PROCLAMATION SINGULARITAIRE": "02_proclamations_singularitaire.md",
    "PROCLAMATION MONADIQUE": "03_proclamations_monadique.md",
    "PROCLAMATION ARCHETYPALE": "04_proclamations_archetypale.md",
    "PROCLAMATION PROTOTYPale": "05_proclamations_prototypale.md",
    "PROCLAMATION PARADIGMATIQUE": "06_proclamations_paradigmatique.md",
    "PROCLAMATION AXIOLOGIQUE": "07_proclamations_axiologique.md",
    "PROCLAMATION CONSTITUTIONNELLE": "08_proclamations_constitutionnelle.md",
    "PROCLAMATION LEGISLATIVE": "09_proclamations_legislative.md",
    "PROCLAMATION CODICILLAIRE": "10_proclamations_codicillaire.md",
    "PROCLAMATION NOTARIEE": "11_proclamations_notariee.md",
    "PROCLAMATION DIPLOMATIQUE": "12_proclamations_diplomatique.md",
    "PROCLAMATION JUDICIAIRE": "13_proclamations_judiciaire.md",
    "PROCLAMATION EXEGETIQUE": "14_proclamations_exegetique.md",
    "PROCLAMATION TALMUDIQUE": "15_proclamations_talmudique.md",
    "PROCLAMATION SCHOLASTIQUE": "16_proclamations_scholastique.md",
}

# Regex: capture tout titre de proclamation h1/h2 avec ou sans emoji et avec "ULTIME"
TITLE_RE = re.compile(r"^\s{0,3}#+\s+.*?PROCLAMATION\s+([A-ZÀ-ÖØ-Ýa-zà-öø-ý\-]+).*?ULTIME", re.IGNORECASE)

def detect_blocks(lines):
    blocks = []
    start = None
    title_raw = None

    for i, line in enumerate(lines):
        m = TITLE_RE.match(line)
        if m:
            # si un bloc était ouvert, on le ferme avant d'ouvrir le suivant
            if start is not None:
                blocks.append((start, i, title_raw))
            start = i
            title_raw = m.group(0)
        else:
            # si on croise un séparateur majeur, on pourrait clôturer (optionnel)
            pass

    # fermer le dernier bloc si ouvert
    if start is not None:
        blocks.append((start, len(lines), title_raw))

    return blocks

def choose_filename(title_line):
    # extrait le mot-clé après "PROCLAMATION"
    m = re.search(r"PROCLAMATION\s+([A-ZÀ-ÖØ-Ýa-zà-öø-ý\-]+)", title_line, re.IGNORECASE)
    key = norm(m.group(0)) if m else ""
    # transforme en clé attendue
    key = re.sub(r"\bULTIME\b", "", key).strip()
    # Uniformise accents/variantes spécifiques:
    key = key.replace("À", "A").replace("É", "E").replace("È", "E").replace("Â", "A").replace("Ê", "E").replace("Î", "I").replace("Ô", "O").replace("Û", "U").replace("Ç", "C")
    # Simplifie pour lookup
    # extrait "PROCLAMATION X"
    m2 = re.search(r"(PROCLAMATION\s+[A-Z\-]+)", key)
    k = m2.group(1) if m2 else ""
    # corrections de quelques variations possibles
    k = k.replace("PROCLAMATION LEGISLATIVE", "PROCLAMATION LEGISLATIVE")
    k = k.replace("PROCLAMATION NOTARIEE", "PROCLAMATION NOTARIEE")
    k = k.replace("PROCLAMATION CODICILLAIRE", "PROCLAMATION CODICILLAIRE")
    k = k.replace("PROCLAMATION ARCHETYPALE", "PROCLAMATION ARCHETYPALE")
    k = k.replace("PROCLAMATION PROTOTYPALE", "PROCLAMATION PROTOTYPale".upper())
    k = k.replace("PROCLAMATION EXEGETIQUE", "PROCLAMATION EXEGETIQUE")
    k = k.replace("PROCLAMATION TALMUDIQUE", "PROCLAMATION TALMUDIQUE")
    k = k.replace("PROCLAMATION SCHOLASTIQUE", "PROCLAMATION SCHOLASTIQUE")
    # lookup
    fname = PREFIX_MAP.get(k)
    return fname

def wrap_with_markers(block_lines, title_norm):
    header_marker = f"# === {title_norm} ULTIME ===\n"
    footer_marker = "# === FIN PROCLAMATION ===\n"
    # évite double balisage si déjà présent
    content_str = "".join(block_lines)
    if "# === FIN PROCLAMATION ===" in content_str and "=== PROCLAMATION" in content_str:
        return block_lines  # déjà balisé
    return [header_marker] + block_lines + [footer_marker]

def main():
    with open(SOURCE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    blocks = detect_blocks(lines)
    if not blocks:
        print("Aucun bloc de proclamation détecté.")
        return

    created = 0
    for (start, end, title_line) in blocks:
        fname = choose_filename(title_line or "")
        if not fname:
            # si inconnu, on saute mais on n'arrête pas tout
            print(f"⚠️ Proclamation non mappée: {title_line.strip() if title_line else 'N/A'}")
            continue

        title_norm = re.search(r"PROCLAMATION\s+[A-ZÀ-ÖØ-Ýa-zà-öø-ý\-]+", title_line, re.IGNORECASE).group(0)
        title_norm = norm(title_norm)  # normalisé (sans accents, en majuscules)

        block_lines = lines[start:end]
        out_lines = wrap_with_markers(block_lines, title_norm)

        out_path = os.path.join(OUTPUT_DIR, fname)
        with open(out_path, "w", encoding="utf-8") as out:
            out.writelines(out_lines)
        created += 1
        print(f"✅ Extrait: {fname}")

    print(f"🎯 Terminé: {created} fichiers créés dans {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
