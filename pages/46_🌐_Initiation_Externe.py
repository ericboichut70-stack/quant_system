# 🌐 Lecture du manifeste d’initiation externe — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="🌐 Initiation externe", layout="wide")
st.title("🌐 Initiation externe — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_initiation_externe.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_manifest_initiation_externe.md"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier manifeste introuvable.")
