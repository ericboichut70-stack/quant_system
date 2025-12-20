# 🔊 Résumé vocal des rôles et usages pour onboarding audio
# 📌 Résultat : audio_roles_summary.wav dans exports/audio/, utilisable pour onboarding vocal par rôle.
import yaml
import pyttsx3

def export_audio_roles_vocal(audio_path="config/bot_registry_audio.yaml", output_path="exports/audio/audio_roles_summary.wav"):
    with open(audio_path, "r") as f:
        audio_index = yaml.safe_load(f)

    summary = "Synthèse des rôles vocaux du projet :\n"
    for filename, meta in audio_index.items():
        summary += f"{filename} — rôle : {meta['rôle']}, usage : {meta['usage']}\n"

    engine = pyttsx3.init()
    engine.save_to_file(summary, output_path)
    engine.runAndWait()
    print(f"✅ Résumé vocal exporté : {output_path}")
