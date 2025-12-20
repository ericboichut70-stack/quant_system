# 📘 Lecture finale
# 🔚 Clôture finale — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="🔚 Clôture Projet", layout="wide")
st.title("🔚 Clôture finale du projet — Private Assistant")

# 📘 Lecture de la synthèse Markdown
md_path = "config/bot_registry_cloture_finale.md"
if os.path.exists(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    st.markdown(md_content)
else:
    st.warning("⚠️ Fichier Markdown de clôture finale introuvable.")

# 🔊 Lecture de la synthèse vocale
audio_path = "config/onboarding_cloture_finale_summary.mp3"
if os.path.exists(audio_path):
    st.audio(audio_path)
else:
    st.warning("⚠️ Synthèse vocale de clôture finale introuvable.")

# 📘 Lecture de bot_registry_cloture_finale.md
bot_registry_cloture_finale.md
