# 📢 Partage des blocs publics et vocaux
import streamlit as st
import os

st.set_page_config(page_title="📢 Diffusion Projet", layout="wide")
st.title("📢 Partage des blocs publics et vocaux — Private Assistant")

st.subheader("📘 Fichiers publics à diffuser")
public_md = [
    "bot_registry_onboarding.md",
    "bot_registry_contracts.md",
    "bot_registry_certification.md"
]
for md in public_md:
    path = os.path.join("exports", md)
    if os.path.exists(path):
        st.markdown(f"- 📄 `{md}`")
    else:
        st.warning(f"⚠️ Fichier manquant : {md}")

st.subheader("🔊 Synthèses vocales à diffuser")
public_audio = [
    "onboarding_manifest_summary.mp3",
    "onboarding_validation_summary.wav",
    "onboarding_certification_summary.mp3"
]
for audio in public_audio:
    path = os.path.join("exports/audio", audio)
    if os.path.exists(path):
        st.markdown(f"**🎧 {audio}**")
        st.audio(path, format="audio/mp3" if audio.endswith(".mp3") else "audio/wav")
    else:
        st.warning(f"⚠️ Fichier audio non trouvé : {audio}")

# Ajout de bot_registry_index_public.yaml
st.subheader("📘 Index public final")

public_index_path = "config/bot_registry_index_public.yaml"
if os.path.exists(public_index_path):
    with open(public_index_path, "r") as f:
        public_index_content = f.read()
    st.text_area("📢 Contenu du fichier index_public", public_index_content, height=300)
else:
    st.warning("⚠️ Fichier index public introuvable.")
