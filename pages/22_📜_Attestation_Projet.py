# 📜 Signature finale et certificat de diffusion
import streamlit as st
import os
from datetime import datetime

st.set_page_config(page_title="📜 Attestation Projet", layout="wide")
st.title("📜 Attestation finale et certificat de diffusion — Private Assistant")

st.subheader("🧾 Certificat de clôture")
version = "1.0.0"
date = datetime.now().strftime("%d %B %Y à %Hh%M")

st.markdown(f"""
✅ **Projet certifié et verrouillé**

- Version : `{version}`
- Date : `{date}`
- Auteur : `Eric`
- Statut : `Soumis et prêt pour diffusion`

Tous les blocs ont été validés, archivés et intégrés dans l’export final.
""")

st.subheader("🔊 Synthèse vocale de clôture")
audio_path = "exports/audio/onboarding_cloture_summary.mp3"
if os.path.exists(audio_path):
    st.audio(audio_path, format="audio/mp3")
else:
    st.warning("⚠️ Fichier audio non trouvé.")

if st.button("🖋️ Signer l’attestation finale"):
    st.success("✅ Attestation signée. Le projet est officiellement clôturé.")

# 🔊 Synthèse vocale dans la page Attestation Projet
st.subheader("🔊 Synthèse vocale d’attestation")

attestation_audio = "exports/audio/onboarding_attestation_summary.wav"
if os.path.exists(attestation_audio):
    st.audio(attestation_audio, format="audio/wav")
    st.success("✅ Synthèse d’attestation prête à l’écoute.")
else:
    st.warning("⚠️ Fichier audio non trouvé.")

# 📘 Ajout de onboarding_attestation_summary.mp3
st.subheader("🔊 Synthèse vocale d’attestation finale (.mp3)")

attestation_audio_mp3 = "exports/audio/onboarding_attestation_summary.mp3"
if os.path.exists(attestation_audio_mp3):
    st.audio(attestation_audio_mp3, format="audio/mp3")
    st.success("✅ Synthèse MP3 d’attestation prête à l’écoute.")
else:
    st.warning("⚠️ Fichier audio non trouvé.")

# 📜 st.subheader("📘 Certificat officiel du projet")

certificat_path = "config/bot_registry_certificat.yaml"
if os.path.exists(certificat_path):
    with open(certificat_path, "r") as f:
        certificat_content = f.read()
    st.text_area("🧾 Contenu du certificat YAML", certificat_content, height=300)
else:
    st.warning("⚠️ Fichier de certificat introuvable.")
Ajout de bot_registry_certificat.yaml

# 📜 Ajout de bot_registry_index_attestation.yaml
st.subheader("📘 Index d’attestation finale")

attestation_index_path = "config/bot_registry_index_attestation.yaml"
if os.path.exists(attestation_index_path):
    with open(attestation_index_path, "r") as f:
        attestation_index_content = f.read()
    st.text_area("📜 Contenu du fichier index_attestation", attestation_index_content, height=300)
else:
    st.warning("⚠️ Fichier index d’attestation introuvable.")

# 🧠 Ajout de bot_registry_index_memoire.yaml
st.subheader("📘 Index mémoire final")

memoire_index_path = "config/bot_registry_index_memoire.yaml"
if os.path.exists(memoire_index_path):
    with open(memoire_index_path, "r") as f:
        memoire_index_content = f.read()
    st.text_area("🧠 Contenu du fichier index_memoire", memoire_index_content, height=300)
else:
    st.warning("⚠️ Fichier index mémoire introuvable.")
