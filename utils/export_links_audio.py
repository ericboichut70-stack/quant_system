# 🔉 Version audio exportable pour onboarding externe
# 📌 Résultat : un fichier .wav dans exports/audio/ prêt à être partagé pour onboarding externe.
import yaml
import pyttsx3

def export_links_audio(link_path="config/bot_registry_links.yaml", output_path="exports/audio/onboarding_links.wav"):
    with open(link_path, "r") as f:
        links = yaml.safe_load(f)

    summary = "Liens et raccourcis du projet :\n"
    for key, meta in links.items():
        summary += f"{meta['label']} : {meta['chemin']}\n"
        if "export_md" in meta:
            summary += f"Export markdown : {meta['export_md']}\n"
        if "capture" in meta:
            summary += f"Capture : {meta['capture']}\n"
        summary += "\n"

    engine = pyttsx3.init()
    engine.save_to_file(summary, output_path)
    engine.runAndWait()
    print(f"✅ Audio exporté : {output_path}")
