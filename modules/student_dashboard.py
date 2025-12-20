# ✅ Interface élève de suivi des validations
import pandas as pd
import streamlit as st
from modules.memory_timeline import build_memory_timeline

st.title("🎓 Tableau de bord élève")

selected_user = st.selectbox("👤 Choisir votre identifiant", user_list)
user_signals = load_signals_for_user(selected_user)
user_feedbacks = load_feedback_for_user(selected_user)

st.subheader("📌 Vos signaux")
st.dataframe(user_signals)

st.subheader("🧑‍🏫 Feedbacks reçus")
st.dataframe(user_feedbacks)

st.subheader("📈 Évolution de vos scénarios")
timeline_df = build_memory_timeline(user_feedbacks)
for scenario in timeline_df["ScenarioType"].unique():
    scenario_df = timeline_df[timeline_df["ScenarioType"] == scenario]
    st.line_chart(scenario_df.set_index("timestamp")["cumulative_score"])

from utils.student_progress import build_student_progress
# 📁 Tableau de progression élève
st.subheader("📈 Votre progression pédagogique")
total, valides, ratio, progress_df = build_student_progress(feedback_df, selected_user)

st.markdown(f"**Total de signaux :** {total}")
st.markdown(f"**Validés :** {valides}")
st.markdown(f"**Taux de validation :** {ratio}%")
st.dataframe(progress_df)

# ✅ Réactivation autonome par l’élève
from modules.scenario_reactivator import reactivate_scenario, save_memory_dict

st.subheader("🔁 Réactivation autonome")

scenario_to_reactivate = st.selectbox("🎭 Scénario désactivé", memory_df[memory_df["IsActive"] == False]["ScenarioType"])
if st.button("✅ Réactiver ce scénario"):
    memory_dict = reactivate_scenario(memory_dict, scenario_to_reactivate)
    save_memory_dict(memory_dict)
    st.success(f"✅ Le scénario '{scenario_to_reactivate}' a été réactivé.")

from modules.personal_recommender import recommend_scenarios
# 📊 Appel module de recommandation personnalisée
st.subheader("🎯 Recommandations pédagogiques personnalisées")
recommendations = recommend_scenarios(feedback_df, memory_dict, selected_user)

for scenario, count, score in recommendations:
    st.markdown(f"✅ **{scenario}** — {count} validations, score mémoire : {score}")

from utils.pedagogical_settings import pedagogical_settings
# Appel interface de paramétrage pédagogique
st.subheader("⚙️ Paramètres pédagogiques")
user_settings = pedagogical_settings()

from utils.pedagogical_settings import pedagogical_settings
from modules.scenario_pathway import build_scenario_pathway
# Appel logique de parcours scénarisé
settings = pedagogical_settings()
pathway = build_scenario_pathway(feedback_df, selected_user, memory_dict, difficulty=settings["difficulty"])

st.subheader("🧭 Parcours scénarisé personnalisé")
for step in pathway:
    st.markdown(f"➡️ **{step['Scenario']}** — {step['Validations']} validations, score mémoire : {step['Score mémoire']}")

from modules.objective_tracker import track_objectives
# Appel module de suivi des objectifs
st.subheader("🎯 Suivi de vos objectifs pédagogiques")
progress = track_objectives(feedback_df, selected_user, user_settings)
for k, v in progress.items():
    st.markdown(f"**{k}** : {v}")

from modules.adaptive_feedback import generate_adaptive_feedback
# Appel logique de feedback adaptatif en temps réel
st.subheader("🧠 Feedback adaptatif en temps réel")
df_validated["Feedback"] = df_validated.apply(
    lambda row: generate_adaptive_feedback(row, selected_user, memory_dict, user_settings), axis=1
)
st.dataframe(df_validated[["ScenarioType", "ConfidenceScore", "Feedback"]])

from utils.option_manager import option_manager
# Appel interface de gestion des options pédagogiques
st.subheader("🛠️ Interface de gestion des options pédagogiques")
user_options = option_manager(selected_user)

# ✅ Appel pour filtrer les scénarios selon le niveau
from modules.multi_level_pathway import assign_level

st.subheader("🧭 Filtrage des scénarios selon ton niveau")
user_level = assign_level(feedback_df, selected_user, coherence_df)
st.markdown(f"**Niveau attribué :** {user_level}")

# Filtrage des scénarios proposés
level_scenarios = {
    "Débutant": ["range", "breakout"],
    "Intermédiaire": ["reversal", "news_spike"],
    "Avancé": ["volatility trap", "liquidity sweep"]
}

available_scenarios = level_scenarios.get(user_level, [])
df_filtered = df_validated[df_validated["ScenarioType"].isin(available_scenarios)]
st.dataframe(df_filtered)

# 📊 Appel interface de coaching hebdomadaire
from modules.weekly_coach import weekly_coaching

st.subheader("📅 Coaching hebdomadaire personnalisé")
coach_report = weekly_coaching(feedback_df, selected_user, memory_dict, user_settings)
for k, v in coach_report.items():
    st.markdown(f"**{k}** : {v}")

# Appel logique de pause pédagogique
from modules.pause_manager import toggle_pedagogical_pause

st.subheader("⏸️ Pause pédagogique")
pause = st.checkbox("Activer la pause pédagogique", value=False)

if st.button("🔄 Mettre à jour le statut"):
    toggle_pedagogical_pause(selected_user, pause)
    st.success("✅ Statut mis à jour.")

# 📊 Appel module de relance intelligente
from modules.smart_nudge import generate_nudge

st.subheader("📬 Relance intelligente")
nudge = generate_nudge(feedback_df, selected_user, memory_dict)
st.markdown(nudge)

# 📊 Appel verrouillage des tailles de compte
from modules.account_size_limiter import get_account_size_options, validate_account_size

st.subheader("💼 Sélection de la taille de compte propfirm")
account_size = st.selectbox("📏 Choisir votre taille de compte", get_account_size_options())

if st.button("✅ Confirmer la taille sélectionnée"):
    if validate_account_size(account_size, user_profile):
        st.success(f"✅ Taille de compte '{account_size}' validée.")
    else:
        st.error("❌ Taille non autorisée pour votre profil.")

from modules.pedagogical_journal import build_pedagogical_journal
# 📊 Appel module de journal pédagogique
st.subheader("📘 Journal pédagogique")
journal_df = build_pedagogical_journal(feedback_df, cross_df, coaching_df, pause_log, selected_user)
st.dataframe(journal_df)

from modules.pre_trade_simulator import simulate_signal
# 📊 Appel logique de simulation pré-trade
st.subheader("🧪 Simulation pré-trade")
df_validated["Simulation"] = df_validated.apply(
    lambda row: simulate_signal(row, memory_dict, user_settings), axis=1
)
st.dataframe(df_validated[["ScenarioType", "ConfidenceScore", "Simulation"]])

from utils.option_manager import option_manager
# Appel interface de gestion des options pédagogiques
st.subheader("🛠️ Interface de gestion des options pédagogiques")
user_options = option_manager(selected_user)

from modules.export_pedagogy import prepare_export
# 📊 Export pédagogique
st.subheader("📤 Export pédagogique")
export_df = prepare_export(feedback_df, cross_df, coaching_df, selected_user)
st.dataframe(export_df)
# Export manuel possible via bouton Streamlit ou interface PDF externe

from modules.pedagogical_pair import assign_binome, load_binomes
# 📊 Appel interface de binôme pédagogique
st.subheader("🧑‍🤝‍🧑 Binôme pédagogique")
partner = st.selectbox("👥 Choisir un binôme", user_list)

if st.button("🤝 Créer le binôme"):
    assign_binome(selected_user, partner)
    st.success(f"✅ Binôme créé entre {selected_user} et {partner}")

st.subheader("📋 Binômes actifs")
binome_df = load_binomes()
st.dataframe(binome_df)

from modules.pedagogical_rewards import assign_rewards
# 📊 Appel module de récompense pédagogique
st.subheader("🏅 Récompenses pédagogiques")
rewards = assign_rewards(feedback_df, binome_scores, tournament_df, selected_user)
for r in rewards:
    st.markdown(r)

from modules.visual_badges import get_visual_badges
# 📊 Appel module de badge visuel
st.subheader("🏅 Badges visuels")
visuals = get_visual_badges(rewards)
for badge in visuals:
    st.markdown(f"{badge['Emoji']} **{badge['Récompense']}** — Niveau : {badge['Niveau']}, Couleur : {badge['Couleur']}")

from modules.narrative_progression import generate_narrative
# 📊 Appel interface de progression narrative
st.subheader("📖 Progression narrative")
narrative = generate_narrative(feedback_df, rewards, selected_user)
st.markdown(narrative)

from modules.badge_gallery import get_badge_catalog
# 📊 Appel interface de galerie de badges
st.subheader("🏅 Galerie des badges pédagogiques")
catalog = get_badge_catalog()
for badge in catalog:
    st.markdown(
        f"{badge['emoji']} **{badge['nom']}** — Niveau : {badge['niveau']}  \n"
        f"_Critère d’obtention_ : {badge['description']}"
    )

from modules.pedagogical_quests import get_available_quests
# 📊 Appel logique de quête pédagogique
st.subheader("🗺️ Quêtes pédagogiques")
quests = get_available_quests(selected_user, feedback_df, memory_dict)
for q in quests:
    st.markdown(
        f"🧩 **{q['titre']}** — Objectif : {q['objectif']}  \n"
        f"🎁 Récompense : {q['récompense']}"
    )

from modules.quest_tracker import track_quests
# 📊 Appel interface de suivi des quêtes
st.subheader("🗺️ Suivi des quêtes pédagogiques")
quest_df = track_quests(selected_user, feedback_df)
st.dataframe(quest_df)

from modules.seasonal_progression import assign_season
# 📊 Appel logique de progression par saison
st.subheader("📆 Progression par saison")
season = assign_season(feedback_df, selected_user)
st.markdown(f"**{selected_user}** est actuellement dans : {season}")

from modules.season_reset import reset_season
# 📊 Appel logique de réinitialisation saisonnière
st.subheader("🔄 Réinitialisation saisonnière")
mode = st.radio("Mode de réinitialisation", ["soft", "hard"])
if st.button("♻️ Réinitialiser la saison"):
    result = reset_season(selected_user, feedback_df, memory_dict, mode)
    st.success(f"✅ Nouvelle saison : {result['season']}")
    st.markdown(result["narrative"])
    for q in result["quests"]:
        st.markdown(f"🧩 **{q['titre']}** — Objectif : {q['objectif']}  \n🎁 Récompense : {q['récompense']}")
    st.markdown(f"🎭 Nouveau rôle : {result['role']}")
    if result["unlocked_scenarios"]:
        st.markdown(f"🔓 Scénarios débloqués : {', '.join(result['unlocked_scenarios'])}")

from modules.seasonal_roles import assign_seasonal_role
# 📊 Appel logique de rôle mentoré par saison
st.subheader("🎭 Rôle pédagogique")
role = assign_seasonal_role(feedback_df, selected_user)
st.markdown(f"**{selected_user}** est actuellement : {role}")
# 🔐 Déblocage automatique: Permissions et scénarios liés au rôle mentoré
role, unlocked_scenarios = assign_seasonal_role(feedback_df, selected_user)
st.markdown(f"**{selected_user}** est actuellement : {role}")
if unlocked_scenarios:
    st.markdown(f"🔓 Scénarios débloqués : {', '.join(unlocked_scenarios)}")

from modules.mentorship_link import assign_mentor, load_mentorships
# 📊 Appel logique de parrainage mentoré
st.subheader("🤝 Parrainage mentoré")
mentor = st.selectbox("👤 Choisir un parrain", user_list)
if st.button("🔗 Lier au parrain"):
    assign_mentor(selected_user, mentor)
    st.success(f"✅ {selected_user} est désormais parrainé par {mentor}")

st.subheader("📋 Liens de parrainage")
mentorship_df = load_mentorships()
st.dataframe(mentorship_df)

from modules.community_badges import assign_community_badges
from modules.community_season import get_active_season
# 📊 Appel logique de badge communautaire
st.subheader("🏅 Badge communautaire")
active = get_active_season()
season_scenarios = active["scenarios"].split(",")

community_badges = assign_community_badges(feedback_df, selected_user, season_scenarios)
for b in community_badges:
    st.markdown(b)

from modules.binome_storyline import record_binome_story
# 📊 Appel logique de narration par binôme
# 🔒 Tu peux afficher ces événements dans une chronologie binôme, une fiche de progression, ou une galerie communautaire.
st.subheader("📖 Narration binôme")
binome = st.multiselect("👥 Membres du binôme", user_list, max_selections=2)
title = st.text_input("🏷️ Titre de l’événement")
scenario = st.selectbox("🎭 Scénario vécu", scenario_list)
outcome = st.text_area("📜 Issue ou apprentissage")

if st.button("📝 Enregistrer l’événement binôme"):
    record_binome_story(binome, title, scenario, outcome)
    st.success("✅ Événement narratif enregistré.")
