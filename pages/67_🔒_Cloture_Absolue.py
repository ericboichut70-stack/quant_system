# 🔒 Lecture du manifeste de clôture absolue — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="🔒 Clôture Absolue", layout="wide")
st.title("🔒 Clôture Absolue — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_cloture_absolue.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_manifest_cloture_absolue.md"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier manifeste introuvable.")
