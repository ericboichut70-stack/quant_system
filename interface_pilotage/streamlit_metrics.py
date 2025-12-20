# 📊 Interface Streamlit — visualisation des métriques globales
import streamlit as st
import yaml

st.set_page_config(page_title="Métriques du bot", layout="wide")
st.title("📈 Métriques globales — Private Assistant")

with open("config/bot_metrics.yaml", "r") as f:
    metrics = yaml.safe_load(f)

st.metric("Modules totaux", metrics["total_modules"])
st.metric("Modules verrouillés", safe_metric(metrics, "verrouillés"))
st.metric("Modules en test", metrics["en_test"])
st.metric("Modules non testés", metrics["non_testés"])
st.metric("Score moyen (verrouillés)", metrics["score_moyen_verrouillés"])
st.metric("Score moyen (en test)", metrics["score_moyen_testés"])
st.metric("Progression globale", f"{metrics['progression_globale'] * 100:.1f}%")

# 🛠️ 🔧 Correction du bug KeyError: 'verrouillés',
# Le fichier bot_metrics.yaml n’a pas été généré ou mis à jour correctement,
# Ajout d'une protection dans streamlit_metrics.py et bot_dashboard.py :
def safe_metric(metrics, key, default=0):
    return metrics.get(key, default)
