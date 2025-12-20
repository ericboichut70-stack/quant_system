# 📋 Export .md de la synthèse complète (liens + rôles + usages)
# 📌 Résultat : bot_registry_onboarding.md dans exports/
import yaml

def export_onboarding_md(links_path="config/bot_registry_links.yaml", audio_path="config/bot_registry_audio.yaml", output_path="exports/bot_registry_onboarding.md"):
    with open(links_path, "r") as f:
        links = yaml.safe_load(f)
    with open(audio_path, "r") as f:
        audio_index = yaml.safe_load(f)

    lines = ["# 🧠 Synthèse Onboarding — Private Assistant\n\n"]

    lines.append("## 🔗 Liens et raccourcis\n")
    for key, meta in links.items():
        lines.append(f"### {meta['label']}\n")
        lines.append(f"- Chemin : `{meta['chemin']}`\n")
        if "export_md" in meta:
            lines.append(f"- Export .md : `{meta['export_md']}`\n")
        if "capture" in meta:
            lines.append(f"- Capture : `{meta['capture']}`\n")
        lines.append("\n")

    lines.append("## 🎙️ Fichiers vocaux\n")
    for filename, meta in audio_index.items():
        lines.append(f"### {filename}\n")
        lines.append(f"- Rôle : {meta['rôle']}\n")
        lines.append(f"- Format : `{meta['format']}`\n")
        lines.append(f"- Source : `{meta['source']}`\n")
        lines.append(f"- Usage : {meta['usage']}\n\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_registry_onboarding.md généré.")
