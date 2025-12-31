import os

DOCS_ROOT = "docs"

def list_docs():
    for root, dirs, files in os.walk(DOCS_ROOT):
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(root, f)

def check_missing_index():
    missing = []
    for root, dirs, files in os.walk(DOCS_ROOT):
        if any(f.endswith(".md") for f in files):
            if "index.md" not in files and "README.md" not in files:
                missing.append(root)
    return missing

def main():
    print("📚 Vérification de la documentation\n")

    print("📄 Fichiers Markdown détectés :")
    for f in list_docs():
        print(" -", f)

    print("\n🔍 Dossiers sans index :")
    missing = check_missing_index()
    if not missing:
        print(" ✔️ Tous les dossiers ont un index.")
    else:
        for m in missing:
            print(" -", m)

if __name__ == "__main__":
    main()
