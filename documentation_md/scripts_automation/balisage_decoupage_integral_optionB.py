# balisage_decoupage_integral_optionB.py
import os, re, unicodedata

SOURCE = "index_consolidated.md"
OUTPUT_DIR = "../corpus_modulaire"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def normaliser(texte: str) -> str:
    """Supprime les accents et normalise en minuscules."""
    texte = unicodedata.normalize("NFKD", texte)
    texte = "".join(ch for ch in texte if not unicodedata.combining(ch))
    texte = texte.lower().strip()
    texte = re.sub(r"\s+", " ", texte)
    return texte

def slug(texte: str) -> str:
    """Transforme un texte en identifiant de fichier (sans espaces ni accents)."""
    texte = normaliser(texte)
    texte = re.sub(r"[^\w\s-]", "", texte)
    return texte.replace(" ", "_")

# Table des proclamations principales
TITRES = {
    "proclamation unitaire": "01_proclamations_unitaire",
    "proclamation singularitaire": "02_proclamations_singularitaire",
    "proclamation monadique": "03_proclamations_monadique",
    "proclamation archetypale": "04_proclamations_archetypale",
    "proclamation prototypale": "05_proclamations_prototypale",
    "proclamation paradigmatique": "06_proclamations_paradigmatique",
    "proclamation axiologique": "07_proclamations_axiologique",
    "proclamation constitutionnelle": "08_proclamations_constitutionnelle",
    "proclamation legislative": "09_proclamations_legislative",
    "proclamation codicillaire": "10_proclamations_codicillaire",
    "proclamation notariee": "11_proclamations_notariee",
    "proclamation diplomatique": "12_proclamations_diplomatique",
    "proclamation judiciaire": "13_proclamations_judiciaire",
    "proclamation exegetique": "14_proclamations_exegetique",
    "proclamation talmudique": "15_proclamations_talmudique",
    "proclamation scholastique": "16_proclamations_scholastique",
}

# Détection des titres de proclamation
REGEX_TITRE = re.compile(r"^\s{0,3}#+\s+.*?proclamation\s+([a-zà-öø-ÿ\-]+).*?ultime", re.IGNORECASE)
REGEX_SOUS_TITRE = re.compile(r"(acte\s+d[’']\w+.*)$", re.IGNORECASE)

def detecter_blocs(lignes):
    blocs = []
    debut, titre = None, None
    for i, ligne in enumerate(lignes):
        if REGEX_TITRE.match(ligne):
            if debut is not None:
                blocs.append((debut, i, titre))
            debut, titre = i, ligne
    if debut is not None:
        blocs.append((debut, len(lignes), titre))
    return blocs

def extraire_sous_titre(lignes, debut, fin):
    """Cherche un sous-titre dans les 20 lignes après le titre."""
    fenetre = lignes[debut:min(fin, debut+20)]
    for ligne in fenetre:
        m = REGEX_SOUS_TITRE.search(ligne)
        if m:
            return m.group(1).strip()
    return "variante"

def chemin_unique(chemin_base: str) -> str:
    """Ajoute un suffixe incrémental si le fichier existe déjà."""
    if not os.path.exists(chemin_base):
        return chemin_base
    racine, ext = os.path.splitext(chemin_base)
    k = 2
    while True:
        nouveau = f"{racine}_{k}{ext}"
        if not os.path.exists(nouveau):
            return nouveau
        k += 1

def main():
    with open(SOURCE, "r", encoding="utf-8") as f:
        lignes = f.readlines()

    blocs = detecter_blocs(lignes)
    if not blocs:
        print("⚠️ Aucun bloc de proclamation détecté.")
        return

    total = 0
    for debut, fin, titre_ligne in blocs:
        titre_norm = normaliser(titre_ligne)
        m = re.search(r"(proclamation\s+[a-z\-]+)", titre_norm)
        cle = m.group(1) if m else ""
        base = TITRES.get(cle)
        if not base:
            print(f"⚠️ Proclamation non mappée: {titre_ligne.strip()}")
            continue

        sous_titre = extraire_sous_titre(lignes, debut, fin)
        slug_sous_titre = slug(sous_titre)
        nom_fichier = f"{base}_{slug_sous_titre}.md"
        chemin = chemin_unique(os.path.join(OUTPUT_DIR, nom_fichier))

        bloc = lignes[debut:fin]
        if "# === FIN PROCLAMATION ===" not in "".join(bloc):
            bloc = [f"# === {cle.upper()} ULTIME ===\n"] + bloc + ["# === FIN PROCLAMATION ===\n"]

        with open(chemin, "w", encoding="utf-8") as out:
            out.writelines(bloc)
        total += 1
        print(f"✅ Extrait: {os.path.basename(chemin)}")

    print(f"🎯 Terminé: {total} fichiers créés dans {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
