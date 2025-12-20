# balisage_decoupage_integral_total.py
import os, re, unicodedata

SOURCE = "index_consolidated.md"
BASE_OUTPUT_DIR = "../documentation_md/corpus_modulaire"

def normaliser(texte: str) -> str:
    texte = unicodedata.normalize("NFKD", texte)
    texte = "".join(ch for ch in texte if not unicodedata.combining(ch))
    texte = texte.lower().strip()
    texte = re.sub(r"\s+", " ", texte)
    return texte

def slug(texte: str) -> str:
    texte = normaliser(texte)
    texte = re.sub(r"[^\w\s-]", "", texte)
    return texte.replace(" ", "_")

# Détection du prochain lot disponible
def prochain_lot(base_dir: str) -> str:
    os.makedirs(base_dir, exist_ok=True)
    lots = [d for d in os.listdir(base_dir) if d.startswith("lot_") and os.path.isdir(os.path.join(base_dir, d))]
    if not lots:
        return os.path.join(base_dir, "lot_1")
    nums = []
    for lot in lots:
        try:
            nums.append(int(lot.split("_")[1]))
        except:
            pass
    prochain_num = max(nums) + 1 if nums else 1
    return os.path.join(base_dir, f"lot_{prochain_num}")

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
    fenetre = lignes[debut:min(fin, debut+20)]
    for ligne in fenetre:
        m = REGEX_SOUS_TITRE.search(ligne)
        if m:
            return m.group(1).strip()
    return "variante"

def chemin_unique(chemin_base: str) -> str:
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

    lot_dir = prochain_lot(BASE_OUTPUT_DIR)
    os.makedirs(lot_dir, exist_ok=True)
    print(f"📂 Extraction vers : {lot_dir}")

    total = 0
    for debut, fin, titre_ligne in blocs:
        titre_norm = normaliser(titre_ligne)
        m = re.search(r"(proclamation\s+[a-z\-]+)", titre_norm)
        cle = m.group(1) if m else "proclamation_inconnue"

        sous_titre = extraire_sous_titre(lignes, debut, fin)
        slug_sous_titre = slug(sous_titre)
        nom_fichier = f"{cle}_{slug_sous_titre}.md"
        chemin = chemin_unique(os.path.join(lot_dir, nom_fichier))

        bloc = lignes[debut:fin]
        if "# === FIN PROCLAMATION ===" not in "".join(bloc):
            bloc = [f"# === {cle.upper()} ULTIME ===\n"] + bloc + ["# === FIN PROCLAMATION ===\n"]

        with open(chemin, "w", encoding="utf-8") as out:
            out.writelines(bloc)
        total += 1
        print(f"✅ Extrait: {os.path.basename(chemin)}")

    print(f"🎯 Terminé: {total} fichiers créés dans {lot_dir}")

if __name__ == "__main__":
    main()
