# 📖 Lecture de l'Index Consolidé Final — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="📖 Index Consolidé Final", layout="wide")
st.title("📖 Index Consolidé Final — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_index_consolide_final.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_index_consolide_final.yaml"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Contenu de l'index consolidé final")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier index consolidé final introuvable.")
