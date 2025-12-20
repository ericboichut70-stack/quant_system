# 📈 Affichage et analyse des scores
# 📈 Simulation des scores — Private Assistant

import streamlit as st
import yaml
import os

st.set_page_config(page_title="📈 Simulation Scoring", layout="wide")
st.title("📈 Analyse des scores par scénario — Private Assistant")

scores_path = "config/bot_registry_scores.yaml"

if os.path.exists(scores_path):
    with open(scores_path, "r") as f:
        scores_data = yaml.safe_load(f)
    scores = scores_data.get("scores", {})
    seuils = scores_data.get("seuils", {})

    st.subheader("📊 Scores par scénario")
    for scenario, score in scores.items():
        st.markdown(f"- **{scenario}** : `{score}` points")

    total = sum(scores.values())
    st.subheader("📈 Score cumulé")
    st.metric(label="Total", value=total)

    statut = "✅ Réussite" if total >= seuils.get("réussite", 80) else (
        "⚠️ Alerte" if total >= seuils.get("alerte", 60) else "❌ Échec"
    )
    st.success(f"Statut global : {statut}")
else:
    st.warning("⚠️ Fichier de scoring introuvable.")
