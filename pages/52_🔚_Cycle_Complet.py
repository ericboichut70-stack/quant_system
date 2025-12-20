# 🔚 Lecture du manifeste de cycle complet — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="🔚 Cycle complet", layout="wide")
st.title("🔚 Cycle complet — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_cycle_complet.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_manifest_cycle_complet.md"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier manifeste introuvable.")
