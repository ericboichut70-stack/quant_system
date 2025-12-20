# 🎧 Créer une version .mp3 pour diffusion contractuelle
# 📌 Résultat : onboarding_manifest_summary.mp3 dans exports/audio/
import pyttsx3
from pydub import AudioSegment

def export_manifest_mp3(output_path="exports/audio/onboarding_manifest_summary.mp3"):
    summary = """
Bienvenue dans le manifeste de Private Assistant.

Ce projet est structuré autour :
- D’un registre versionné des livrables
- D’un contrat d’engagements techniques
- D’un fichier de signatures validant chaque étape
- D’attestations de conformité et de validation mentor

Chaque bloc est consultable dans la page Manifeste Interactif et Contrats Projet.
"""

    temp_wav = "exports/audio/temp_manifest.wav"
    engine = pyttsx3.init()
    engine.save_to_file(summary, temp_wav)
    engine.runAndWait()

    sound = AudioSegment.from_wav(temp_wav)
    sound.export(output_path, format="mp3")
    print(f"✅ Audio MP3 exporté : {output_path}")
