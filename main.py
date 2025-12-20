import streamlit as st

st.set_page_config(page_title="Professeur SMC", layout="wide")

st.title("🧠 Professeur SMC – Lancement centralisé")

st.markdown("Bienvenue dans la version alpha du bot pédagogique. Choisissez un module à lancer ci-dessous.")

option = st.radio("📂 Modules disponibles :", [
    "Dashboard principal",
    "Test des scénarios pédagogiques",
    "Radar des marchés",
    "Replay pédagogique",
    "Explication des signaux"
])

if option == "Dashboard principal":
    st.markdown("👉 Lancez dans PowerShell : `streamlit run dashboard.py`")

elif option == "Test des scénarios pédagogiques":
    st.markdown("👉 Lancez dans PowerShell : `streamlit run scripts/test_scenarios.py`")

elif option == "Radar des marchés":
    st.markdown("Module : `market_radar.py` – intégré dans dashboard")

elif option == "Replay pédagogique":
    st.markdown("Module : `replay_mode.py` – activable dans dashboard")

elif option == "Explication des signaux":
    st.markdown("Module : `explainable_ai.py` – utilisé dans test_scenarios")
