# 🎧 Générer la version .mp3 de la synthèse publique
# 📌 Résultat : onboarding_public_summary.mp3 dans exports/audio/
import pyttsx3
from pydub import AudioSegment

def export_public_mp3(output_path="exports/audio/onboarding_public_summary.mp3"):
    summary = """
Bienvenue dans la version publique du projet Private Assistant.

Ce projet propose :
- Une documentation claire et consolidée
- Des synthèses vocales pour l’onboarding
- Un manifeste versionné et validé
- Une archive complète pour audit et diffusion

Tous les fichiers publics sont listés dans le registre de diffusion.
"""

    temp_wav = "exports/audio/temp_public.wav"
    engine = pyttsx3.init()
    engine.save_to_file(summary, temp_wav)
    engine.runAndWait()

    sound = AudioSegment.from_wav(temp_wav)
    sound.export(output_path, format="mp3")
    print(f"✅ Audio MP3 exporté : {output_path}")
