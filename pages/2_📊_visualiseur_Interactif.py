# 📊 Visualiseur_Interactif.py
# EX-streamlit_map_viewer.py renommé pour créer un raccourci dans le menu principal
# (navigation multi-page Streamlit)
# 🌳 Visualiseur Streamlit en arborescence
import streamlit as st
import yaml

st.set_page_config(page_title="🌳 Cartographie interactive", layout="wide")
st.title("🌳 Visualiseur interactif — Private Assistant")

with open("config/bot_registry_map.yaml", "r") as f:
    map_data = yaml.safe_load(f)

for file, content in map_data.items():
    with st.expander(f"📁 {file}", expanded=False):
        for key, items in content.items():
            st.markdown(f"**🔸 {key.capitalize()}**")
            for item in items:
                st.markdown(f"- {item}")
