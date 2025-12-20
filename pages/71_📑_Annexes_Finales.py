# 📑 Lecture des Annexes Finales — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="📑 Annexes Finales", layout="wide")
st.title("📑 Annexes Finales — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_annexes_finales.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_manifest_annexes_final.md"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier manifeste introuvable.")
