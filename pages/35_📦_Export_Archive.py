# 📦Lecture du manifeste
# 📦 Export Archive — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="📦 Export Archive", layout="wide")
st.title("📦 Export complet — Private Assistant")

# 📘 Lecture du manifeste Markdown (optionnel)
md_path = "config/bot_registry_index_archive.yaml"
if os.path.exists(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Index de l’archive ZIP")
        st.code(f.read(), language="yaml")
else:
    st.warning("⚠️ Fichier d’index d’archive introuvable.")

# 🔊 Lecture de la synthèse vocale
audio_path = "config/onboarding_export_archive_summary.mp3"
if os.path.exists(audio_path):
    st.subheader("🔊 Synthèse vocale de l’export")
    st.audio(audio_path)
else:
    st.warning("⚠️ Synthèse vocale de l’export introuvable.")
