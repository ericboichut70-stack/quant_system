# 📋 Export .md de bot_registry_audio.yaml pour documentation externe
import yaml

def export_audio_md(audio_path="config/bot_registry_audio.yaml", output_path="exports/bot_registry_audio.md"):
    with open(audio_path, "r") as f:
        audio_index = yaml.safe_load(f)

    lines = ["# 🎙️ Index des fichiers vocaux — Private Assistant\n\n"]
    for filename, meta in audio_index.items():
        lines.append(f"## {filename}\n")
        lines.append(f"- Rôle : {meta['rôle']}\n")
        lines.append(f"- Format : `{meta['format']}`\n")
        lines.append(f"- Source : `{meta['source']}`\n")
        lines.append(f"- Usage : {meta['usage']}\n\n")

    with open(output_path, "w") as f:
        f.writelines(lines)

    print("✅ bot_registry_audio.md généré.")
