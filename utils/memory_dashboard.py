# 📊 Interface de visualisation de memory_dict
st.subheader("🧠 Mémoire pédagogique du Professeur")

memory_dict = {
    "breakout": 2,
    "range": -1,
    "news_spike": -3,
    "reversal": 1
}  # À charger dynamiquement plus tard

memory_df = pd.DataFrame(memory_dict.items(), columns=["Scénario", "Score mémoire"])
st.dataframe(memory_df)

# Filtre par score
score_threshold = st.slider("🎯 Score mémoire minimal à afficher", -5, 5, -2)
filtered_df = memory_df[memory_df["Score mémoire"] >= score_threshold]
st.dataframe(filtered_df)
st.bar_chart(filtered_df.set_index("Scénario")["Score mémoire"])

# 📊 Visualisation graphique
st.subheader("📊 Graphique des scores mémoire")
st.bar_chart(memory_df.set_index("Scénario")["Score mémoire"])

# Suggestions pédagogiques
from modules.memory_evolution import suggest_adjustments_from_memory
suggestions = suggest_adjustments_from_memory(memory_dict)
for s in suggestions:
    st.markdown(s)

# 📊 Appel d’évolution des scores mémoire par scénario, dans le temps, à partir des feedbacks enregistrés.
from modules.memory_timeline import build_memory_timeline

feedback_df = pd.read_csv("utils/feedback_log.txt", sep="|", names=["timestamp", "feedback", "decision", "ScenarioType"])
timeline_df = build_memory_timeline(feedback_df)

st.subheader("📈 Évolution des scores mémoire")
selected_scenario = st.selectbox("🎭 Choisir un scénario", timeline_df["ScenarioType"].unique())
scenario_df = timeline_df[timeline_df["ScenarioType"] == selected_scenario]

st.line_chart(scenario_df.set_index("timestamp")["cumulative_score"])

# Appel de réactivation manuelle d'un scénario désactivé par l'utilisatur
from modules.scenario_reactivator import reactivate_scenario, save_memory_dict

st.subheader("🔁 Réactivation manuelle d’un scénario")

scenario_to_reactivate = st.selectbox("🎭 Choisir un scénario à réactiver", memory_df["Scénario"])
if st.button("✅ Réactiver le scénario"):
    memory_dict = reactivate_scenario(memory_dict, scenario_to_reactivate)
    save_memory_dict(memory_dict)
    st.success(f"✅ Le scénario '{scenario_to_reactivate}' a été réactivé.")
