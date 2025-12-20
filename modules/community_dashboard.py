from modules.community_hub import publish_signal, load_community_signals
# 📊 Appel interface communautaire de publication et scoring croisé
st.subheader("🌍 Publication communautaire")
scenario = st.selectbox("🎭 Scénario", scenario_list)
score = st.slider("📊 Score", 0, 10, 5)
comment = st.text_area("📝 Commentaire")

if st.button("📨 Publier"):
    publish_signal(selected_user, scenario, score, comment)
    st.success("✅ Signal publié dans la communauté.")

st.subheader("📋 Signaux communautaires")
community_df = load_community_signals()
st.dataframe(community_df)

from modules.community_roles import get_community_roles
# 📊 Appel interface de rôle communautaire
st.subheader("🎭 Rôles communautaires")
role_df = pd.DataFrame(get_community_roles(feedback_df, user_list))
st.dataframe(role_df)

from modules.community_season import define_community_season, get_active_season
# 📊 Appel logique de saison communautaire
st.subheader("🌍 Définir une saison communautaire")
season_name = st.text_input("🏷️ Nom de la saison")
scenarios = st.multiselect("🎭 Scénarios clés", scenario_list)
start = st.date_input("📅 Début")
end = st.date_input("📅 Fin")

if st.button("📢 Lancer la saison communautaire"):
    define_community_season(season_name, scenarios, start, end)
    st.success("✅ Saison communautaire enregistrée.")

st.subheader("📆 Saison communautaire active")
active = get_active_season()
st.markdown(f"**{active['name']}** — {active['dates']}")
st.markdown(f"🎭 Scénarios : {active['scenarios']}")

from modules.seasonal_ranking import compute_seasonal_ranking
from modules.community_season import get_active_season
# 📊 Appel interface de classement saisonnier
# 🔒 Tu peux lier ce classement à une publication ou une récompense collective.
st.subheader("📊 Classement saisonnier")
active = get_active_season()
season_name = active["name"]
season_scenarios = active["scenarios"].split(",")

ranking_df = compute_seasonal_ranking(feedback_df, season_scenarios, season_name)
st.dataframe(ranking_df)

from modules.community_gallery import build_community_gallery
# 📊 Appel interface de galerie communautaire
# 🔒 Tu peux enrichir avec des filtres par saison, rôle ou binôme.
st.subheader("🏛️ Galerie communautaire")
gallery_df = build_community_gallery()
st.dataframe(gallery_df)

from modules.seasonal_trophy import assign_seasonal_trophy
from modules.community_season import get_active_season
# 📊 Appel logique de trophée saisonnier
st.subheader("🏆 Trophée saisonnier")
active = get_active_season()
season_scenarios = active["scenarios"].split(",")

trophy = assign_seasonal_trophy(feedback_df, season_scenarios, user_list)
st.markdown(f"🏆 **{trophy['Trophée de saison']}** attribué à **{trophy['Utilisateur']}** avec {trophy['Score']} validations.")

from modules.community_reactivation import generate_reactivation_messages
# 📊 Appel logique de relance communautaire
st.subheader("📣 Relance communautaire")
reactivation_msgs = generate_reactivation_messages(feedback_df, user_list)
for msg in reactivation_msgs:
    st.markdown(msg)

from modules.season_closure import generate_season_closure
from modules.seasonal_trophy import assign_seasonal_trophy
from modules.seasonal_ranking import compute_seasonal_ranking
from modules.community_season import get_active_season
from modules.community_gallery import build_community_gallery
# 📊 Appel interface de célébration de fin de saison
active = get_active_season()
season_scenarios = active["scenarios"].split(",")

trophy = assign_seasonal_trophy(feedback_df, season_scenarios, user_list)
ranking_df = compute_seasonal_ranking(feedback_df, season_scenarios, active["name"])
badge_log = build_community_gallery()

closure_msg = generate_season_closure(active, trophy, ranking_df, badge_log)
st.subheader("🎉 Célébration de fin de saison")
st.markdown(closure_msg)

from modules.season_transition import prepare_season_transition
from modules.community_season import get_active_season
# 📊 Appel interface de transition vers la nouvelle saison
st.subheader("🌅 Transition vers une nouvelle saison")
old_season = get_active_season()
new_name = st.text_input("🏷️ Nom de la nouvelle saison")
new_scenarios = st.multiselect("🎭 Scénarios clés", scenario_list)
start_date = st.date_input("📅 Date de lancement")

if st.button("🚀 Lancer la nouvelle saison"):
    transition = prepare_season_transition(old_season, new_name, new_scenarios, start_date)
    st.success("✅ Transition enregistrée.")
    st.markdown(transition["Message"])

from modules.scenario_voting import record_vote, tally_votes
# 📊 Appel logique de vote communautaire pour les scénarios
st.subheader("🗳️ Vote communautaire pour les scénarios")
scenario_choice = st.selectbox("🎭 Choisis ton scénario préféré", scenario_list)
if st.button("🗳️ Voter"):
    record_vote(selected_user, scenario_choice)
    st.success("✅ Vote enregistré.")

st.subheader("📊 Résultats du vote")
vote_df = tally_votes()
st.dataframe(vote_df)

from modules.temporary_roles import assign_temporary_role
# 📊 Appel logique de rôle communautaire temporaire
st.subheader("🎭 Rôle communautaire temporaire")
user = st.selectbox("👤 Membre", user_list)
role = st.text_input("🎭 Rôle à attribuer")
duration = st.slider("⏳ Durée (jours)", 1, 30, 7)

if st.button("🎯 Attribuer le rôle"):
    result = assign_temporary_role(user, role, duration)
    st.success(f"✅ Rôle attribué à {result['Utilisateur']} : {result['Rôle']} (jusqu’au {result['Expire le']})")

from modules.rotating_roles import assign_rotating_role
# 📊 Appel interface de rôle tournant
st.subheader("🎭 Rôle tournant communautaire")
user = st.selectbox("👤 Membre", user_list)
role = st.selectbox("🎯 Rôle à attribuer", ["Animateur de saison", "Validateur communautaire", "Parrain de binôme", "Archiviste pédagogique"])
start = st.date_input("📅 Début")
end = st.date_input("📅 Fin")

if st.button("🔁 Attribuer le rôle tournant"):
    result = assign_rotating_role(user, role, start, end)
    st.success(f"✅ {result['Rôle']} attribué à {result['Utilisateur']} pour la période {result['Période']}")

from modules.collective_storyline import propose_story_event, load_storyline
# 📊 Appel logique de scénarisation collective
st.subheader("📖 Scénarisation collective")
title = st.text_input("🏷️ Titre de l’événement")
description = st.text_area("📜 Description immersive")
if st.button("📝 Proposer l’événement"):
    propose_story_event(selected_user, title, description)
    st.success("✅ Événement scénarisé proposé.")

st.subheader("📚 Narration communautaire en cours")
story_df = load_storyline()
st.dataframe(story_df)

from modules.story_chapter_validation import propose_chapter, validate_chapter
# 📊 Appel interface de chapitre validé
# 🔒 Tu peux afficher les chapitres validés dans une frise ou une galerie narrative.
st.subheader("📖 Proposer un chapitre narratif")
title = st.text_input("🏷️ Titre du chapitre")
content = st.text_area("📜 Contenu narratif")
if st.button("📝 Proposer le chapitre"):
    propose_chapter(selected_user, title, content)
    st.success("✅ Chapitre proposé.")

st.subheader("✅ Valider un chapitre")
chapter_to_validate = st.selectbox("📖 Chapitre à valider", proposed_chapter_titles)
if st.button("✅ Valider ce chapitre"):
    validate_chapter(chapter_to_validate, selected_user)
    st.success(f"✅ Chapitre validé : {chapter_to_validate}")
