# 🧪 Panneau Streamlit — test d’un module en direct
import streamlit as st
import yaml

st.set_page_config(page_title="Test de module", layout="wide")
st.title("🧪 Tester un module — Private Assistant")

with open("config/module_registry.yaml", "r") as f:
    registry = yaml.safe_load(f)

modules = [name for name in registry.keys()]
selected = st.selectbox("Sélectionner un module à tester", modules)

st.markdown(f"### 📦 Module : `{selected}`")
st.markdown(f"- Statut : **{registry[selected]['status']}**")
st.markdown(f"- Export : {'✅' if registry[selected]['export'] else '❌'}")
st.markdown(f"- Replay : {'✅' if registry[selected]['replay'] else '❌'}")

if st.button("🧪 Lancer test simulé"):
    st.info(f"Test simulé lancé pour `{selected}` — résultat fictif : Score 82")
