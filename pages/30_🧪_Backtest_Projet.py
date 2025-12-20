# 🧪 Moteur de simulation
# 🧪 Backtest du projet Private Assistant — lecture des scénarios, scores et relecture

import streamlit as st
import yaml
import os

st.set_page_config(page_title="🧪 Backtest Projet", layout="wide")
st.title("🧪 Simulation et scoring — Private Assistant")

# 📁 Fichiers à charger
paths = {
    "Scénarios": "config/bot_registry_scenarios.yaml",
    "Scores": "config/bot_registry_scores.yaml",
    "Relecture": "config/bot_registry_replay.yaml"
}

data = {}

for label, path in paths.items():
    st.subheader(f"📄 {label}")
    if not os.path.exists(path):
        st.warning(f"⚠️ Fichier introuvable : {path}")
        continue
    with open(path, "r") as f:
        data[label] = yaml.safe_load(f)
    st.code(yaml.dump(data[label], allow_unicode=True), language="yaml")

# 📊 Calcul du score total
if "Scores" in data and "Scénarios" in data:
    scores = data["Scores"].get("scores", {})
    seuils = data["Scores"].get("seuils", {})
    total = sum(scores.values())
    st.subheader("📊 Score total")
    st.metric(label="Score cumulé", value=total)

    statut = "✅ Réussite" if total >= seuils.get("réussite", 80) else (
        "⚠️ Alerte" if total >= seuils.get("alerte", 60) else "❌ Échec"
    )
    st.success(f"Statut : {statut}")

# 🔁 Séquence de relecture
if "Relecture" in data:
    st.subheader("🔁 Séquence de relecture")
    for step in data["Relecture"].get("replay_sequence", []):
        st.markdown(f"- 🔁 {step}")

# 📘 Synthèse Markdown
# 🧪 Synthèse finale du backtest — Private Assistant

## 📅 Date
**10 novembre 2025**

## 🧾 Signataire
**Eric**

---

## ✅ Modules activés

- `30_🧪_Backtest_Projet.py` — moteur de simulation
- `31_📈_Simulation_Scoring.py` — affichage des scores
- `32_🔁_Replay_Validation.py` — relecture des intégrations

---

## 📄 Fichiers de référence

- `bot_registry_scenarios.yaml` — cas de test
- `bot_registry_scores.yaml` — règles de scoring
- `bot_registry_replay.yaml` — logique de relecture
- `bot_registry_backtest.yaml` — index de simulation

---

## 📊 Résultat du scoring

- Score cumulé : **100**
- Statut : ✅ Réussite

---

## 🔁 Relecture des intégrations

- Tous les scénarios ont été rejoués
- Les scores ont été recalculés
- Les synthèses ont été vérifiées
- Les index sont cohérents
- Aucune anomalie détectée

---

## 📦 Usage

- Audit pédagogique
- Simulation mentor
- Archivage final
- Préparation à la certification communautaire

---

## 🏁 Conclusion

Le cycle de backtest est complet, verrouillé et validé.  
**Private Assistant est prêt pour la certification communautaire et la diffusion pédagogique.**

# 🔊 Synthèse vocale
Synthèse finale du backtest du système Private Assistant.

Les modules de simulation, scoring et relecture ont été activés.  
Tous les scénarios ont été rejoués.  
Les scores sont consolidés.  
Le statut global est : réussite.

Le système est prêt pour certification communautaire et diffusion pédagogique.  
Private Assistant est verrouillé, validé, et historiquement complet.
