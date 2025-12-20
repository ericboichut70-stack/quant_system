# 📁 Tous les fichiers validés, audio et documents
import streamlit as st
import os

st.set_page_config(page_title="📦 Export Final", layout="wide")
st.title("📦 Export consolidé — Private Assistant")

st.subheader("📘 Fichiers de validation")
validation_files = [
    "bot_registry_manifest.yaml",
    "bot_registry_archive.yaml",
    "bot_registry_validation.yaml",
    "bot_registry_submission.yaml",
    "bot_registry_certification.md"
]
for file in validation_files:
    path = os.path.join("config" if file.endswith(".yaml") else "exports", file)
    if os.path.exists(path):
        st.markdown(f"- 📄 `{file}`")
    else:
        st.warning(f"⚠️ Fichier manquant : {file}")

st.subheader("🔊 Synthèses vocales")
audio_files = [
    "onboarding_manifest_summary.mp3",
    "onboarding_certification_summary.mp3",
    "onboarding_submission_summary.mp3",
    "onboarding_cloture_summary.wav"
]
for audio in audio_files:
    path = os.path.join("exports/audio", audio)
    if os.path.exists(path):
        st.markdown(f"**🎧 {audio}**")
        st.audio(path, format="audio/mp3" if audio.endswith(".mp3") else "audio/wav")
    else:
        st.warning(f"⚠️ Fichier audio non trouvé : {audio}")

st.subheader("📦 Archive complète")
zip_path = "exports/export_all.zip"
if os.path.exists(zip_path):
    with open(zip_path, "rb") as f:
        st.download_button(
            label="📥 Télécharger l’archive finale",
            data=f,
            file_name="PrivateAssistant_Archive.zip",
            mime="application/zip"
        )
else:
    st.warning("⚠️ Archive ZIP introuvable.")

# 🔊 Synthèse de clôture dans la page Export Final
st.subheader("🔊 Synthèse vocale de clôture")

cloture_audio = "exports/audio/onboarding_cloture_summary.wav"
if os.path.exists(cloture_audio):
    st.audio(cloture_audio, format="audio/wav")
    st.success("✅ Synthèse de clôture prête à l’écoute.")
else:
    st.warning("⚠️ Fichier audio non trouvé.")

# 🎧 Intégration de onboarding_export_summary.wav
# Cela permet de centraliser toutes les synthèses dans une seule page d’export,
# avec écoute directe et vérification de présence.
st.subheader("🔊 Synthèse vocale de l’export consolidé")

export_audio = "exports/audio/onboarding_export_summary.wav"
if os.path.exists(export_audio):
    st.audio(export_audio, format="audio/wav")
    st.success("✅ Synthèse d’export prête à l’écoute.")
else:
    st.warning("⚠️ Fichier audio non trouvé.")

# 📦 Ajout du ZIP
st.subheader("📦 Archive ZIP consolidée")

zip_path = "exports/export_all.zip"
if os.path.exists(zip_path):
    with open(zip_path, "rb") as f:
        st.download_button(
            label="📥 Télécharger l’archive complète",
            data=f,
            file_name="PrivateAssistant_Export.zip",
            mime="application/zip"
        )
    st.success("✅ Archive ZIP prête à être diffusée.")
else:
    st.warning("⚠️ Archive ZIP introuvable.")

# 📜 Ajout de bot_registry_export_vocal.yaml
st.subheader("📘 Index des fichiers audio exportés")

export_vocal_path = "config/bot_registry_export_vocal.yaml"
if os.path.exists(export_vocal_path):
    with open(export_vocal_path, "r") as f:
        export_vocal_content = f.read()
    st.text_area("🔊 Contenu du fichier export vocal", export_vocal_content, height=300)
else:
    st.warning("⚠️ Fichier export vocal introuvable.")

# 📦 Ajout de bot_registry_index_zip.yaml
st.subheader("📘 Index final du ZIP exporté")

zip_index_path = "config/bot_registry_index_zip.yaml"
if os.path.exists(zip_index_path):
    with open(zip_index_path, "r") as f:
        zip_index_content = f.read()
    st.text_area("📦 Contenu du fichier index ZIP", zip_index_content, height=300)
else:
    st.warning("⚠️ Fichier index ZIP introuvable.")

# 📦 Ajout de bot_registry_index_export.yaml
st.subheader("📘 Index d’export final")

export_index_path = "config/bot_registry_index_export.yaml"
if os.path.exists(export_index_path):
    with open(export_index_path, "r") as f:
        export_index_content = f.read()
    st.text_area("📦 Contenu du fichier index_export", export_index_content, height=300)
else:
    st.warning("⚠️ Fichier index d’export introuvable.")
