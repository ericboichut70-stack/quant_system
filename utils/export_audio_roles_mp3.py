# 🎧 Générer une version .mp3 du résumé des rôles
# 📌 Résultat : audio_roles_summary.mp3 dans exports/audio/
import yaml
import pyttsx3
from pydub import AudioSegment

def export_audio_roles_mp3(audio_path="config/bot_registry_audio.yaml", output_path="exports/audio/audio_roles_summary.mp3"):
    with open(audio_path, "r") as f:
        audio_index = yaml.safe_load(f)

    summary = "Synthèse des rôles vocaux du projet :\n"
    for filename, meta in audio_index.items():
        summary += f"{filename} — rôle : {meta['rôle']}, usage : {meta['usage']}\n"

    temp_wav = "exports/audio/temp_roles.wav"
    engine = pyttsx3.init()
    engine.save_to_file(summary, temp_wav)
    engine.runAndWait()

    sound = AudioSegment.from_wav(temp_wav)
    sound.export(output_path, format="mp3")
    print(f"✅ Audio MP3 exporté : {output_path}")
