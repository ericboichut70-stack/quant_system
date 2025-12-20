# 📘 Génération d'un export .md de bot_registry_links.yaml
import yaml

def export_links_md(link_path="config/bot_registry_links.yaml", output_path="exports/bot_registry_links.md"):
    with open(link_path, "r") as f:
        links = yaml.safe_load(f)

    lines = ["# 🔗 Liens et raccourcis — Private Assistant\n\n"]
    for key, meta in links.items():
        lines.append(f"## {meta['label']}\n")
        lines.append(f"- Chemin : `{meta['chemin']}`\n")
        if "export_md" in meta:
            lines.append(f"- Export .md : `{meta['export_md']}`\n")
        if "capture" in meta:
            lines.append(f"- Capture : `{meta['capture']}`\n")
        lines.append("\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_registry_links.md généré.")
