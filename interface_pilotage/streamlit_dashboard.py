# 📊 Interface Streamlit — visualisation des modules activés
import streamlit as st
import yaml

st.set_page_config(page_title="Private Assistant", layout="wide")
st.title("📊 Modules activés — Private Assistant")

with open("config/module_registry.yaml", "r") as f:
    registry = yaml.safe_load(f)

locked = {k: v for k, v in registry.items() if v["status"] == "verrouillé"}

st.subheader("🔒 Modules verrouillés")
for name, data in locked.items():
    st.markdown(f"**{name}** — Score: {data['score']} | Export: {data['export']} | Replay: {data['replay']}")

st.success(f"{len(locked)} module(s) verrouillé(s) et activé(s)")

# Lancement possible avec: streamlit run interface_pilotage/streamlit_dashboard.py.
