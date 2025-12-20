# 📊 Interface Streamlit — visualisation de activation_history.yaml
import streamlit as st
import yaml

st.set_page_config(page_title="Historique d’activation", layout="wide")
st.title("📜 Historique des activations — Private Assistant")

with open("config/activation_history.yaml", "r") as f:
    history = yaml.safe_load(f)

for session in history:
    st.subheader(f"🕒 {session['date']}")
    st.markdown(f"- Mode : **{session['mode']}**")
    st.markdown(f"- Export : {'✅' if session['export'] else '❌'}")
    st.markdown(f"- Replay : {'✅' if session['replay'] else '❌'}")
    st.markdown("**Modules activés :**")
    for m in session["modules"]:
        st.markdown(f"• {m}")
