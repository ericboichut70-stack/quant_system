import pandas as pd
import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.scenario_builder import build_scenario, validate_scenario
from modules.explainable_ai import explain_signal
from modules.replay_mode import replay_signals

# Dictionnaire de recommandations
parameter_guidance = {
    "RiskReward": "💡 Un ratio > 2.0 est souvent considéré comme optimal pour les setups à forte conviction.",
    "ExpectancyThreshold": "📈 Un seuil d'espérance > 0.2 filtre les actifs avec un potentiel mathématique positif.",
    "Mitigated": "🧠 Les signaux non mitigés sont plus bruts, mais parfois plus risqués.",
    "StructureType": "📚 'bullish' et 'bearish' sont les bases, mais 'range' permet d'explorer les zones de neutralité.",
    "Volume": "🔊 Un volume élevé confirme l'intérêt du marché, mais un faible volume peut signaler une manipulation."
}

# 📥 Chargement des données 
df = pd.read_csv("data/test_data.csv")  # ou df_combined si déjà en mémoire
st.write("📊 Colonnes du DataFrame :", df.columns.tolist())

# 📘 Définition des scénarios
scenarios = {
    "Breakout haussier avec FVG et OB": {
        "type": "breakout",
        "conditions": [
            "StructureType == 'bullish'",
            "BOS == True",
            "FVGType == 'bullish'",
            "OrderBlock == True",
            "Mitigated == False"
        ],
        "expected": "Signal BuyCombined avec explication claire"
    },
    "ChOCh baissier avec mitigation": {
        "type": "reversal",
        "conditions": [
            "StructureType == 'bearish'",
            "ChOCh == True",
            "FVGType == 'bearish'",
            "Mitigated == True"
        ],
        "expected": "Signal SellCombined avec POI actif"
    },
    "Range avec fausse cassure et retour": {
        "type": "range",
        "conditions": [
            "StructureType == 'range'",
            "LiquidityZone == 'high'",
            "AggressionType == 'buy'",
            "Mitigated == True"
        ],
        "expected": "Signal BuyCombined avec explication pédagogique"
    }
}
scenario = {
    "name": "Filtrage par gain optimal",
    "type": "gain_filter",
    "conditions": [
        "SignalSuccess == 1",
        "RiskReward > 1.5"
    ],
    "expected": "high_expectancy"
}
scenarios["Signal mitigé mais ratio faible"] = {
    "type": "reversal",
    "conditions": [
        "Mitigated == True",
        "RiskReward < 1.2",
        "SignalSuccess == 0"
    ],
    "expected": "Signal rejeté ou à éviter"
}

scenarios["Signal combiné avec faible volume"] = {
    "type": "breakout",
    "conditions": [
        "OrderBlock == True",
        "FVGType == 'bullish'",
        "Volume < 1000",
        "SignalSuccess == 1"
    ],
    "expected": "Signal BuyCombined mais à confirmer par contexte"
}

# 🎛️ Interface Streamlit
st.title("🧪 Tests de scénarios pédagogiques")

selected_scenario = st.selectbox("🎭 Choisir un scénario à tester", list(scenarios.keys()))
scenario = scenarios[selected_scenario]

# 🧩 Validation du scénario et poucentage seuil Risk/Reward
df_validated = validate_scenario(df, scenario)
rr_threshold = st.slider("🎚️ Seuil Risk/Reward (%)", min_value=0.5, max_value=3.0, value=1.5, step=0.1)
st.markdown(parameter_guidance["RiskReward"])

scenario = {
    "name": "Filtrage par gain optimal",
    "type": "gain_filter",
    "conditions": [
        "SignalSuccess == 1",
        f"RiskReward > {rr_threshold}"
    ],
    "expected": "high_expectancy"
}

# 🧠 Explication des signaux
df_validated["Explanation"] = df_validated.apply(explain_signal, axis=1)

# 📊 Affichage des résultats
st.subheader("📋 Signaux détectés dans le scénario")
st.dataframe(df_validated.filter(items=["timestamp", "ScenarioType", "ExpectedOutcome", "Explanation"], axis=1, errors="ignore"))

# 🧠 Intégration pédagogique des curseurs
expectancy_threshold = st.slider("📈 Seuil d'espérance mathématique", min_value=0.0, max_value=1.0, value=0.2, step=0.05)
st.markdown(parameter_guidance["ExpectancyThreshold"])

volume_threshold = st.slider("🔊 Seuil de volume minimal", min_value=0, max_value=5000, value=1000, step=100)
st.markdown(parameter_guidance["Volume"])

mitigation_filter = st.selectbox("🧠 Filtrer par mitigation", ["Tous", "Mitigated", "Non mitigated"])
if mitigation_filter == "Mitigated":
    st.markdown(parameter_guidance["Mitigated"])
elif mitigation_filter == "Non mitigated":
    st.markdown("⚠️ Les signaux non mitigés peuvent être plus risqués.")

structure_choice = st.selectbox("📚 Type de structure", ["bullish", "bearish", "range"])
st.markdown(parameter_guidance["StructureType"])

# 1. 🎛️ Curseurs pédagogiques
# (définis ici, pas dans scenario_builder.py)s
rr_threshold = st.slider("🎚️ Seuil Risk/Reward (%)", 0.5, 3.0, 1.5, 0.1)
volume_threshold = st.slider("🔊 Volume minimal", 0, 5000, 1000, 100)
structure_choice = st.selectbox("📚 Structure", ["bullish", "bearish", "range"])
mitigation_filter = st.selectbox("🧠 Mitigation", ["Tous", "Mitigated", "Non mitigated"])

def suggest_adjustment(rr, structure):
    if rr > 4.0 and structure == "range":
        return "⚠️ Ratio élevé en contexte de range : probabilité d’entrée faible, risque de faux signal."
    elif rr < 1.0:
        return "📉 Ratio trop faible : risque de perte mathématique même en cas de succès."
    return "✅ Ratio cohérent avec la structure choisie."

# 2. # 🧠 Construction du scénario dynamique
# (à partir des curseurs)

conditions = [f"RiskReward > {rr_threshold}", f"Volume > {volume_threshold}", f"StructureType == '{structure_choice}'"]
if mitigation_filter == "Mitigated":
    conditions.append("Mitigated == True")
elif mitigation_filter == "Non mitigated":
    conditions.append("Mitigated == False")

scenario = {
    "name": "Scénario personnalisé",
    "type": "custom",
    "conditions": conditions,
    "expected": "Signal filtré selon réglages manuels"
}

# 🤖 Mode autonome
auto_mode = st.checkbox("🤖 Laisser le bot choisir le scénario optimal")

if auto_mode:
    from modules.bot_logic import bot_select_best_scenario  # à créer si besoin
    scenario = bot_select_best_scenario(df)
    st.markdown(f"🧠 Scénario choisi : {scenario['name']}")
    st.markdown(f"📚 Justification : {scenario['expected']}")

# 3. 🧩 Validation du scénario

# 4. 🧠 Explication des signaux
df_validated["Explanation"] = df_validated.apply(explain_signal, axis=1)

# 5. 📊 Affichage des résultats
st.dataframe(df_validated.filter(items=["timestamp", "ScenarioType", "ExpectedOutcome", "Explanation"], axis=1, errors="ignore"))

# Sélecteur de replay pédagogique
replay_mode = st.selectbox("🎬 Mode de replay", ["standard", "slow", "explain"])
replay_msgs = replay_signals(df_validated, speed=0.1, mode=replay_mode)

# 🧩 Validation du scénario
df_validated = validate_scenario(df, scenario)

# 🧠 Mise à jour de la mémoire du bot
from modules.bot_memory import update_bot_memory, get_memory_summary
nb_erreurs = update_bot_memory(df_validated)
st.markdown(get_memory_summary())

for name, sc in scenarios.items():
    st.subheader(f"🧪 Test du scénario : {name}")
    df_result = validate_scenario(df, sc)
    st.dataframe(df_result.filter(items=["timestamp", "ScenarioType", "ExpectedOutcome"], axis=1, errors="ignore"))

# 🧩 Application enrichissement du dashboard
df_validated["SignalType"] = df_validated.apply(assign_signal_type, axis=1)

# 🧩 Application fonction score de confiance de 0 à 10
df_validated["ConfidenceScore"] = df_validated.apply(compute_confidence_score, axis=1)

#  Affichage du signal lumineux du Professeur
df_validated["LiveSignal"] = df_validated.apply(live_professor_signal, axis=1)

# ✅ Application interface “live du Professeur” — 4 signaux lumineux
df_validated["LiveSignal"] = df_validated.apply(lambda row: live_professor_signal(row), axis=1)
