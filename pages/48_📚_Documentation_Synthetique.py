# 📚 Lecture du manifeste de documentation synthétique — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="📚 Documentation synthétique", layout="wide")
st.title("📚 Documentation synthétique — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_documentation_synthetique.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_manifest_documentation_synthetique.md"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier manifeste introuvable.")
