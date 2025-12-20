# 📦 Lecture du manifeste d’archivage définitif — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="📦 Archivage définitif", layout="wide")
st.title("📦 Archivage définitif — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_archive_definitive.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_manifest_archive_finale.md"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier manifeste introuvable.")
