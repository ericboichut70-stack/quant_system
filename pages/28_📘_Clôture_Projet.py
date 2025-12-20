# 📘 Page de lecture dédiée à la clôture finale du projet Private Assistant
# 🔐 Clôture finale — Private Assistant

import streamlit as st
import os

st.title("🔐 Clôture finale — Private Assistant")

# 📄 Lecture du fichier Markdown
md_path = "config/bot_registry_cloture_finale.md"
if os.path.exists(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    st.markdown(md_content)
else:
    st.warning("⚠️ Fichier Markdown de clôture introuvable.")

# 🌐 Lecture du fichier HTML (optionnel)
html_path = "config/bot_registry_cloture_finale.html"
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=800, scrolling=True)
else:
    st.info("ℹ️ Fichier HTML de clôture non trouvé. Lecture Markdown uniquement.")
