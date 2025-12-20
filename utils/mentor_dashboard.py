## 📊 Structure du tableau de bord mentor-élève
st.subheader("📊 Tableau de bord mentor-élève")

selected_user = st.selectbox("👤 Choisir un élève", user_list)
user_signals = load_signals_for_user(selected_user)
mentor_feedbacks = load_feedback_for_user(selected_user)

st.dataframe(user_signals)
st.dataframe(mentor_feedbacks)

# 📊 Grouper par scénario, score ou date
st.subheader("📊 Vue pédagogique mentor-élève")

group_mode = st.selectbox("🗂️ Grouper par", ["Scénario", "Score", "Date"])
if group_mode == "Scénario":
    grouped = mentor_feedback_df.groupby("ScenarioType").count()
elif group_mode == "Score":
    grouped = mentor_feedback_df.groupby("ConfidenceScore").count()
else:
    mentor_feedback_df["Date"] = pd.to_datetime(mentor_feedback_df["timestamp"]).dt.date
    grouped = mentor_feedback_df.groupby("Date").count()

st.dataframe(grouped)

# Affichage sélectif des signaux pertinents selon les critères choisis
from modules.signal_filter import filter_signals

st.subheader("🧠 Filtrer les signaux pédagogiques")

selected_market = st.selectbox("🌍 Marché", ["forex", "crypto", "indices", "actions"], index=0)
selected_context = st.selectbox("📊 Contexte", ["range", "breakout", "news", "reversal"], index=0)
min_score = st.slider("🎯 Score de confiance minimal", 0, 10, 5)

df_filtered = filter_signals(df_validated, market=selected_market, context=selected_context, min_score=min_score)
st.dataframe(df_filtered)

# 📊 Tableau de suivi des demandes
from modules.mentor_approver import load_reactivation_requests, approve_reactivation

st.subheader("📋 Suivi des demandes de réactivation")

requests_df = load_reactivation_requests()
st.dataframe(requests_df)

selected_request = st.selectbox("📌 Choisir une demande", requests_df["scenario"].unique())
if st.button("✅ Valider la réactivation"):
    memory_dict = approve_reactivation(selected_request, memory_dict)
    st.success(f"✅ Le scénario '{selected_request}' a été réactivé.")

# Appel de validation mentorale avant réactivation
st.subheader("🧑‍🏫 Demande de réactivation mentorale")

scenario = st.selectbox("🎭 Scénario désactivé", memory_df[memory_df["IsActive"] == False]["ScenarioType"])
mentor = st.text_input("👤 Nom du mentor")
comment = st.text_area("📝 Justification", height=100)

if st.button("📨 Soumettre la demande"):
    request_mentor_validation(scenario, mentor, comment)
    st.success("✅ Demande envoyée au mentor.")

from modules.feedback_stats import compute_feedback_stats
# 📊 Appel statistiques pédagogiques
feedback_df = pd.read_csv("utils/feedback_log.txt", sep="|", names=["timestamp", "feedback", "decision", "ScenarioType", "mentor"])

st.subheader("📊 Statistiques des feedbacks")
mode = st.selectbox("🧭 Mode d’analyse", ["global", "scenario", "mentor", "decision"])
stats_df = compute_feedback_stats(feedback_df, mode)
st.dataframe(stats_df)

from modules.mentor_collab import load_mentor_feedback, submit_mentor_feedback
# 📊 Appel de collaboration mentorale
st.subheader("🤝 Collaboration mentorale")

mentor_name = st.text_input("👤 Nom du mentor")
scenario = st.selectbox("🎭 Scénario à commenter", df_validated["ScenarioType"].unique())
decision = st.selectbox("🧠 Décision", ["Valider", "Rejeter", "À revoir"])
comment = st.text_area("📝 Commentaire", height=100)

if st.button("📨 Soumettre le feedback collaboratif"):
    submit_mentor_feedback(str(datetime.now()), scenario, mentor_name, decision, comment)
    st.success("✅ Feedback mentoral enregistré.")

# Affichage des feedbacks croisés
feedbacks_df = load_mentor_feedback()
st.dataframe(feedbacks_df)

# 📊 Appel du Module de score communautaire
from modules.community_score import compute_community_score

st.subheader("🌐 Score communautaire des scénarios")
community_df = compute_community_score(feedbacks_df)
st.dataframe(community_df)

from modules.certification_engine import evaluate_certification
# 🧩 📊 Appel du module de certification
st.subheader("🎓 Certification pédagogique des élèves")
cert_df = evaluate_certification(feedback_df)
st.dataframe(cert_df)

from modules.parrainage import assign_parrain, load_parrainage
# ✅ Appel de parrainage
st.subheader("🧑‍🤝‍🧑 Parrainage entre élèves")

user = st.selectbox("👤 Élève à parrainer", user_list)
parrain = st.text_input("🧑 Parrain désigné")

if st.button("🤝 Enregistrer le parrainage"):
    assign_parrain(user, parrain)
    st.success(f"✅ {parrain} est maintenant parrain de {user}")

st.subheader("📋 Relations de parrainage")
parrainage_df = load_parrainage()
st.dataframe(parrainage_df)

from modules.cross_validation import submit_cross_validation, load_cross_validations
# 📊 Appel module de validation croisée
st.subheader("🔁 Validation croisée")

scenario = st.selectbox("🎭 Scénario à valider", df_validated["ScenarioType"].unique())
validator = st.text_input("👤 Validateur")
user = st.selectbox("👤 Élève concerné", user_list)
decision = st.selectbox("🧠 Décision", ["Valider", "Rejeter", "À revoir"])
comment = st.text_area("📝 Commentaire", height=100)

if st.button("📨 Soumettre la validation croisée"):
    submit_cross_validation(scenario, validator, user, decision, comment)
    st.success("✅ Validation croisée enregistrée.")

st.subheader("📋 Historique des validations croisées")
cross_df = load_cross_validations()
st.dataframe(cross_df)

# 📊 Logique de progression collective
from modules.collective_progress import compute_collective_progress

progress_df = compute_collective_progress(feedback_df, cross_df)
st.subheader("🌍 Progression collective de la communauté")
st.dataframe(progress_df)


from modules.coherence_engine import compute_coherence
# 📊 Appel module de cohérence mentor/parrain/bot
coherence_df = compute_coherence(feedback_df, cross_df, df_validated)
st.subheader("📐 Cohérence mentor/parrain/bot par scénario")
st.dataframe(coherence_df)

from modules.evolving_score import compute_evolving_score
# 📊 Appel logique de score collectif évolutif
evolving_df = compute_evolving_score(feedback_df, cross_df, df_validated, coherence_df)
st.subheader("📊 Score collectif évolutif des scénarios")
st.dataframe(evolving_df)

from modules.dynamic_deactivator import evaluate_scenario_deactivation
# 📊 Appel module de désactivation dynamique
to_deactivate = evaluate_scenario_deactivation(memory_dict, evolving_df, coherence_df)
for scenario in to_deactivate:
    memory_dict[scenario] = -5  # Désactivation forcée
save_memory_dict(memory_dict)
st.success(f"✅ Scénarios désactivés dynamiquement : {', '.join(to_deactivate)}")

from utils.pedagogical_settings import pedagogical_settings
# 📊 Appel interface de paramétrage pédagogique
st.subheader("⚙️ Paramètres pédagogiques")
user_settings = pedagogical_settings()

# ✅ Ajout du selected_user dans les appels croisés
# 👉 Le mentor peut ainsi visualiser ou ajuster les paramètres pédagogiques d’un élève spécifique.
selected_user = st.selectbox("👤 Élève à superviser", user_list)
user_settings = pedagogical_settings(selected_user)

from utils.option_manager import option_manager
# 📊 Appel interface de gestion des options pédagogiques
st.subheader("🛠️ Interface de gestion des options pédagogiques")
user_options = option_manager(selected_user)

from certification_collab import evaluate_collaborative_certification
# 📊 Appel logique de certification collaborative
st.subheader("🎓 Certification collaborative")
user = st.selectbox("👤 Élève à certifier", user_list)
mentor_approval = st.checkbox("✅ Mentor approuve la certification")

cert_report = evaluate_collaborative_certification(feedback_df, cross_df, memory_dict, user, mentor_approval)
for k, v in cert_report.items():
    st.markdown(f"**{k}** : {v}")

from group_pathway import build_group_pathway
# 📊 Appel progression scénarisée par groupe
group_members = st.multiselect("👥 Sélectionner les membres du groupe", user_list)
group_df = build_group_pathway(feedback_df, group_members)

st.subheader("🧭 Parcours scénarisé du groupe")
st.dataframe(group_df)

from modules.collective_simulator import simulate_group_signals
# 📊 Appel simulation collective
group_signals = [
    {"user": "Alice", "ScenarioType": "breakout", "ConfidenceScore": 8},
    {"user": "Bob", "ScenarioType": "range", "ConfidenceScore": 5},
    {"user": "Charlie", "ScenarioType": "reversal", "ConfidenceScore": 3}
]

sim_results = simulate_group_signals(group_signals, memory_dict)
st.subheader("🧪 Simulation collective")
for res in sim_results:
    st.markdown(res)
# 📊 Appel module de défi mentoré
from modules.mentor_challenge import launch_mentor_challenge, load_challenges

st.subheader("🎯 Défi mentoré")
scenario = st.selectbox("🎭 Scénario imposé", scenario_list)
goal = st.slider("🎯 Objectif de validations", 1, 20, 5)
duration = st.slider("⏳ Durée (jours)", 1, 14, 7)

if st.button("🚀 Lancer le défi"):
    launch_mentor_challenge(selected_mentor, scenario, goal, duration)
    st.success("✅ Défi lancé.")

st.subheader("📋 Défis en cours")
challenge_df = load_challenges()
st.dataframe(challenge_df)

from modules.binome_scoring import compute_binome_score
# 📊 Appel module de scoring binôme
st.subheader("📊 Scoring des binômes pédagogiques")
binome_scores = compute_binome_score(feedback_df, "utils/binome_log.txt", memory_dict)
st.dataframe(binome_scores)

from modules.tournament_hub import launch_tournament, compute_tournament_scores
# 📊 Appel interface de tournoi pédagogique
st.subheader("🏆 Lancer un tournoi pédagogique")
t_name = st.text_input("🎯 Nom du tournoi")
t_scenarios = st.multiselect("🎭 Scénarios imposés", scenario_list)
t_duration = st.slider("⏳ Durée (jours)", 1, 14, 7)

if st.button("🚀 Lancer le tournoi"):
    launch_tournament(t_name, t_scenarios, t_duration)
    st.success("✅ Tournoi lancé.")

st.subheader("📋 Classement des tournois")
tournament_df = compute_tournament_scores(feedback_df, "utils/tournament_log.txt")
st.dataframe(tournament_df)

from modules.ranking_publisher import publish_ranking, load_published_rankings
# 📊 Appel interface de publication des classements
st.subheader("📢 Publication d’un classement")
title = st.text_input("🏷️ Titre du classement")
comment = st.text_area("📝 Commentaire ou contexte")
ranking_df = binome_scores  # ou tournament_df, ou autre

if st.button("📨 Publier le classement"):
    publish_ranking(title, ranking_df, comment)
    st.success("✅ Classement publié.")

st.subheader("📋 Classements publiés")
published = load_published_rankings()
for line in published:
    st.markdown(line)

from modules.season_reset import reset_season
# 📊 Appel interface de réinitialisation saisonnière
st.subheader("🔄 Réinitialisation saisonnière")
mode = st.radio("Mode de réinitialisation", ["soft", "hard"])
if st.button("♻️ Réinitialiser la saison"):
    new_season = reset_season(selected_user, feedback_df, mode)
    st.success(f"✅ Nouvelle saison attribuée : {new_season}")

from modules.mentor_cross_validation import cross_validate_signal
# 📊 Appel interface de validation croisée mentor-parrain
st.subheader("🔁 Validation croisée mentor-parrain")
user = st.selectbox("👤 Filleul à valider", user_list)
scenario = st.selectbox("🎭 Scénario", scenario_list)
decision = st.radio("✅ Décision", ["Valider", "Refuser"])
comment = st.text_area("📝 Commentaire")

if st.button("📨 Valider le signal"):
    cross_validate_signal(selected_mentor, user, scenario, decision, comment)
    st.success("✅ Validation croisée enregistrée.")

from modules.alliance_progression import alliance_progress
# 📊 Appel logique de progression par alliance
st.subheader("🤝 Progression par alliance")
members = st.multiselect("👥 Membres de l’alliance", user_list)
if members:
    alliance = alliance_progress(feedback_df, members)
    st.markdown(f"✅ Validations collectives : {alliance['Total validations']}")
    st.markdown(f"🎭 Scénarios dominants : {', '.join(alliance['Scénarios dominants'])}")
    st.markdown(f"🏅 Badge collectif : {alliance['Badge collectif']}")

from modules.collective_rewards import assign_collective_reward
# 📊 Appel interface de récompense collective
st.subheader("🏅 Récompense collective")
members = st.multiselect("👥 Membres du groupe", user_list)
if members:
    reward = assign_collective_reward(feedback_df, members)
    st.markdown(f"👥 Groupe : {', '.join(reward['Membres'])}")
    st.markdown(f"✅ Validations : {reward['Validations']}")
    st.markdown(f"🎭 Scénarios communs : {', '.join(reward['Scénarios communs'])}")
    st.markdown(f"🏅 Récompense : {reward['Récompense collective']}")

from modules.interpair_quests import generate_interpair_quest
# 📊 Appel logique de quêtes inter-binômes
st.subheader("🧩 Quête inter-binôme")
binome1 = st.multiselect("👥 Binôme 1", user_list)
binome2 = st.multiselect("👥 Binôme 2", user_list)
if binome1 and binome2:
    quest = generate_interpair_quest(binome1, binome2, feedback_df)
    st.markdown(f"🧩 Objectif : {quest['Objectif']}")
    st.markdown(f"🎁 Récompense : {quest['Récompense']}")

from modules.interpair_challenge import launch_interpair_challenge, load_interpair_challenges
# 📊 Appel interface de défi inter-binôme
st.subheader("⚔️ Défi inter-binôme")
binome1 = st.multiselect("👥 Binôme 1", user_list)
binome2 = st.multiselect("👥 Binôme 2", user_list)
scenario = st.selectbox("🎭 Scénario imposé", scenario_list)
goal = st.slider("🎯 Objectif de validations", 5, 30, 10)
duration = st.slider("⏳ Durée (jours)", 1, 14, 7)

if st.button("🚀 Lancer le défi"):
    launch_interpair_challenge(binome1, binome2, scenario, goal, duration)
    st.success("✅ Défi inter-binôme lancé.")

st.subheader("📋 Défis inter-binômes en cours")
challenge_df = load_interpair_challenges()
st.dataframe(challenge_df)

from modules.scenario_launchpad import launch_scenario
# 📊 Appel interface de lancement scénarisé
st.subheader("🚀 Lancement scénarisé")
name = st.text_input("🏷️ Nom du scénario")
description = st.text_area("📖 Description immersive")
goal = st.slider("🎯 Objectif de validations", 5, 30, 10)
duration = st.slider("⏳ Durée (jours)", 1, 14, 7)
reward = st.text_input("🎁 Récompense")

if st.button("🚀 Lancer le scénario"):
    result = launch_scenario(name, description, goal, duration, reward)
    st.success(f"✅ Scénario lancé : {result['Nom']}")
    st.markdown(f"📖 {result['Description']}")
    st.markdown(f"🎯 Objectif : {result['Objectif']} — 🗓️ Deadline : {result['Deadline']} — 🎁 Récompense : {result['Récompense']}")
