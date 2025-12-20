# ♾️ Lecture de l'Infinitude Finale — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="♾️ Infinitude Finale", layout="wide")
st.title("♾️ Infinitude Finale — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_infinitude_finale.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_manifest_infinitude_finale.md"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier manifeste introuvable.")
