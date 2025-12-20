# 🗄️ Lecture du manifeste de transmission historique — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="🗄️ Transmission historique", layout="wide")
st.title("🗄️ Transmission historique — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_transmission_historique.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_manifest_transmission_historique.md"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier manifeste introuvable.")
