import os

def fix_imports(root_dir="."):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                except UnicodeDecodeError:
                    continue  # Ignore les fichiers non UTF-8

                new_content = content.replace("from modules.", "from modules.")
                new_content = new_content.replace("from architecture.", "from architecture.")
                new_content = new_content.replace("from pedagogy.", "from pedagogy.")

                if new_content != content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✅ Corrigé : {filepath}")

if __name__ == "__main__":
    fix_imports()
