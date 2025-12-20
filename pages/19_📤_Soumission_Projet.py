# 📤 Diffusion vers mentor, archive ou communauté
import streamlit as st
import os

st.set_page_config(page_title="📤 Soumission Projet", layout="wide")
st.title("📤 Diffusion vers mentor, archive ou communauté — Private Assistant")

st.subheader("📦 Archive complète")
zip_path = "exports/export_all.zip"
if os.path.exists(zip_path):
    with open(zip_path, "rb") as f:
        st.download_button(
            label="📥 Télécharger l’archive complète",
            data=f,
            file_name="PrivateAssistant_Archive.zip",
            mime="application/zip"
        )
else:
    st.warning("⚠️ Archive ZIP introuvable.")

st.subheader("📘 Fichiers publics")
public_files = [
    "bot_registry_onboarding.md",
    "bot_registry_contracts.md",
    "bot_registry_certification.md"
]
for file in public_files:
    path = os.path.join("exports", file)
    if os.path.exists(path):
        st.markdown(f"- 📄 `{file}`")
    else:
        st.warning(f"⚠️ Fichier manquant : {file}")

st.subheader("🔊 Synthèses vocales")
public_audio = [
    "onboarding_manifest_summary.mp3",
    "onboarding_certification_summary.mp3",
    "onboarding_public_summary.mp3"
]
for audio in public_audio:
    path = os.path.join("exports/audio", audio)
    if os.path.exists(path):
        st.markdown(f"**🎧 {audio}**")
        st.audio(path, format="audio/mp3")
    else:
        st.warning(f"⚠️ Fichier audio non trouvé : {audio}")

# 📤 Bouton “Soumettre vers mentor” avec horodatage
from datetime import datetime

st.subheader("📤 Soumission officielle")

if st.button("✅ Soumettre vers mentor"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.success(f"🧾 Soumission enregistrée le {timestamp}")
    st.markdown("📘 Tous les blocs publics sont prêts pour diffusion et audit.")

# 📤 Synthèse dans la page Soumission Projet
st.subheader("🔊 Synthèse vocale de soumission")

submission_audio = "exports/audio/onboarding_submission_summary.mp3"
if os.path.exists(submission_audio):
    st.audio(submission_audio, format="audio/mp3")
    st.success("✅ Synthèse de soumission prête à l’écoute.")
else:
    st.warning("⚠️ Fichier audio non trouvé.")

# 📤 Ajout de bot_registry_index_soumission.yaml
st.subheader("📘 Index de soumission finale")

soumission_index_path = "config/bot_registry_index_soumission.yaml"
if os.path.exists(soumission_index_path):
    with open(soumission_index_path, "r") as f:
        soumission_index_content = f.read()
    st.text_area("📤 Contenu du fichier index_soumission", soumission_index_content, height=300)
else:
    st.warning("⚠️ Fichier index de soumission introuvable.")
