# 🧑‍🏫 Interface mentor_interface.py — test, score, commentaire
import streamlit as st
import yaml

st.set_page_config(page_title="🧑‍🏫 Interface Mentor", layout="wide")
st.title("🧑‍🏫 Interface de validation mentor — Private Assistant")

with open("config/module_registry.yaml", "r") as f:
    registry = yaml.safe_load(f)

locked = {k: v for k, v in registry.items() if v["status"] == "verrouillé"}
selected = st.selectbox("Sélectionner un module verrouillé", list(locked.keys()))

st.markdown(f"### 📦 Module : `{selected}`")
st.markdown(f"- Score actuel : {locked[selected]['score']}")
st.markdown(f"- Export : {'✅' if locked[selected]['export'] else '❌'}")
st.markdown(f"- Replay : {'✅' if locked[selected]['replay'] else '❌'}")

new_score = st.slider("Score mentor", 0, 100, locked[selected]["score"])
comment = st.text_area("Commentaire mentor")

if st.button("✅ Valider le module"):
    registry[selected]["score"] = new_score
    with open("config/module_registry.yaml", "w") as f:
        yaml.dump(registry, f)
    st.success(f"Module `{selected}` mis à jour avec score {new_score}")
