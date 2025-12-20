import os
import re

def scan_docstrings_and_comments(directory="modules"):
    audit_log = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                for i, line in enumerate(lines):
                    # Docstrings triple quotes
                    if re.search(r'"""|\'\'\'', line):
                        audit_log.append((path, i + 1, line.strip()))
                    # Inline comments
                    elif "#" in line and not line.strip().startswith("#!"):
                        audit_log.append((path, i + 1, line.strip()))

    return audit_log

def save_audit_log(log, output="utils/audit_notes.md"):
    with open(output, "a", encoding="utf-8") as f:
        f.write("\n## 🔍 Audit automatique\n")
        for path, line_num, content in log:
            f.write(f"- `{path}` ligne {line_num} → {content}\n")

if __name__ == "__main__":
    log = scan_docstrings_and_comments()
    save_audit_log(log)
    print("✅ Audit terminé. Résultats ajoutés à audit_notes.md")
