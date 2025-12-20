# 🙏 Lecture des Remerciements Finaux — Private Assistant

import streamlit as st
import os

st.set_page_config(page_title="🙏 Remerciements Finaux", layout="wide")
st.title("🙏 Remerciements Finaux — Private Assistant")

# 🖼️ Bannière visuelle
st.image("assets/banner_remerciements_finaux.png", use_column_width=True)

# 📘 Lecture du texte
txt_path = "documentation_md/bot_registry_manifest_remerciements_final.md"
if os.path.exists(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        st.subheader("📘 Texte source")
        st.text(f.read())
else:
    st.warning("⚠️ Fichier manifeste introuvable.")
