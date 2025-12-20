# 🏛️ Lecture de la Clôture Magistrale Finale — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="🏛️ Clôture Magistrale Finale", layout="wide")
st.title("🏛️ Clôture Magistrale Finale — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_cloture_magistrale_finale.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_manifest_cloture_magistrale_finale.md"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier manifeste introuvable.")
