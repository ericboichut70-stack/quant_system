# 📡 Lecture du manifeste de diffusion pédagogique — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="📡 Diffusion pédagogique", layout="wide")
st.title("📡 Diffusion pédagogique — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_diffusion_pedagogique.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_manifest_diffusion_pedagogique.md"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier texte introuvable.")

# 🔊 Lecture audio
audio_path = "config/onboarding_manifest_diffusion_pedagogique.mp3"
if os.path.exists(audio_path):
    st.subheader("🔊 Lecture vocale")
    st.audio(audio_path)
else:
    st.warning("⚠️ Fichier audio introuvable.")
