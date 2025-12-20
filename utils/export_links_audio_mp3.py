# 🎙️ Générer une version .mp3 pour diffusion externe
# 📌 Résultat : onboarding_links.mp3 dans exports/audio/, prêt pour diffusion externe.
import yaml
from pydub import AudioSegment
import pyttsx3

def export_links_audio_mp3(link_path="config/bot_registry_links.yaml", output_path="exports/audio/onboarding_links.mp3"):
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

    # Temp WAV file
    temp_wav = "exports/audio/temp_onboarding.wav"
    engine = pyttsx3.init()
    engine.save_to_file(summary, temp_wav)
    engine.runAndWait()

    # Convert to MP3
    sound = AudioSegment.from_wav(temp_wav)
    sound.export(output_path, format="mp3")
    print(f"✅ Audio MP3 exporté : {output_path}")
