# 📖 README — Scripts de balisage et découpage

🎯 Objectif

Ce dossier contient les scripts de découpage et d’indexation des proclamations. Ils ont évolué par étapes successives. Cette note interne clarifie leur rôle et précise lequel doit être utilisé désormais.

🗂️ Scripts de balisage/découpage

1. balisage_decoupage_integral.py
Première version historique.

Fonction : découper uniquement les 16 proclamations principales.

Limites : ne gère pas les variantes ni les proclamations supplémentaires (Épilogue, Cosmographique, etc.).

Statut actuel : obsolète. Conservé uniquement comme trace pédagogique.

2 balisage_decoupage_integral_optionB.py
Version intermédiaire.

Fonction : ajoute le sous‑titre dans le nom du fichier et gère les doublons par suffixe (_2,_3…).

Limites : ne couvre pas les proclamations non mappées.

Statut actuel : obsolète. Conservé comme étape de transition.

3 balisage_decoupage_integral_total.py
Version finale et complète.

Fonction :

Découpe toutes les proclamations (les 16 principales + toutes les autres).

Ajoute le sous‑titre dans le nom du fichier.

Ajoute un suffixe incrémental en cas de doublon.

Résultat : corpus complet, auditable et indexé automatiquement.

Statut actuel : script de référence. 👉 C’est le seul script à utiliser désormais pour tout découpage.

📌 Indexation
generate_index_master.py : génère automatiquement 00_index_master.md avec la liste complète des proclamations extraites.

Les doublons sont différenciés par suffixe (_2,_3…).

Le fichier maître se trouve dans documentation_md/00_index_master.md.

✅ Consigne finale
Utiliser uniquement balisage_decoupage_integral_total.py pour tout nouveau découpage.

Conserver les deux autres scripts (integral.py et optionB.py) comme archives pédagogiques, mais ne pas les exécuter en production.

Vérifier systématiquement que 00_index_master.md est bien peuplé après chaque cycle.

📌 Procédure de cycle complet (à insérer dans ton README)

Voici une version claire et verrouillée, en 4 étapes, pour ne plus douter du chemin à suivre :

Découpage du corpus

Exécuter :
python balisage_decoupage_integral_total.py
Résultat : extraction de toutes les proclamations (principales et supplémentaires) dans corpus_modulaire/.

Indexation automatique

Exécuter :
python generate_index_master.py
Résultat : mise à jour de documentation_md/00_index_master.md avec la liste complète des proclamations extraites.

Validation

Exécuter :
python validate_extracted_files.py
Résultat : contrôle de cohérence et détection des doublons ou anomalies.

Cycle complet

Pour enchaîner automatiquement toutes les étapes :
python run_all.py
Résultat : découpage, indexation et validation en une seule commande.

📊 Mini‑plan de suivi — Intégration progressive des 10 000 lignes

Lot intégré (≈ 1 000 lignes) Découpage OK (total.py) Validation OK (validate_extracted_files.py)Indexation OK (generate_index_master.py)

Lot 1 (20 001 → 21 000)                ☐                   ☐                                       ☐
Lot 2 (21 001 → 22 000)                ☐                   ☐                                       ☐
Lot 3 (22 001 → 23 000)                ☐                   ☐                                       ☐
Lot 4 (23 001 → 24 000)                ☐                   ☐                                       ☐
Lot 5 (24 001 → 25 000)                ☐                   ☐                                       ☐
Lot 6 (25 001 → 26 000)                ☐                   ☐                                       ☐
Lot 7 (26 001 → 27 000)                ☐                   ☐                                       ☐
Lot 8 (27 001 → 28 000)                ☐                   ☐                                       ☐
Lot 9 (28 001 → 29 000)                ☐                   ☐                                       ☐
Lot 10 (29 001 → 30 000)               ☐                   ☐                                       ☐

✅ Mode d’emploi

Ajoute 1 000 lignes dans index_consolidated.md.
Lance le découpage : python balisage_decoupage_integral_total.py
Valide les fichiers extraits : python validate_extracted_files.py
Mets à jour l’index maître : python generate_index_master.py
Coche les cases correspondantes dans le tableau.
Passe au lot suivant.

🎯 Résultat attendu

Tu avances par paliers contrôlés.
Chaque lot est validé avant de passer au suivant.
Tu gardes une trace claire et auditable de l’avancement.
Tu évites tout blocage massif et tu restes maître du rythme.

📊 Suivi combiné

Tu peux associer le tableau de suivi (dans ton README) avec cette organisation :

Lot Dossier  Découpage OK  Validation OK Indexation OK
1   lot_1    ☐            ☐             ☐
2   lot_2    ☐            ☐             ☐
…    …       ☐            ☐             ☐

👉 Tu coches les cases au fur et à mesure, et tu sais immédiatement dans quel dossier se trouvent les fichiers du lot validé.

⚡ Procédure cycle complet

1. Ajouter ~1000 lignes dans scripts_automation/index_consolidated.md
2. Exécuter : python balisage_decoupage_integral_total.py   # découpage automatique vers lot_1
3. Exécuter : python validate_extracted_files.py            # validation et contrôle de cohérence
4. Exécuter : python generate_index_master.py               # mise à jour de documentation_md/00_index_master.md
