# 🚀 Onboarding — Bienvenue dans le Projet Quant System

Ce guide te permet de prendre en main le projet rapidement et efficacement.

---

## 🧭 1. Comprendre la structure

Le projet est organisé en familles fonctionnelles :

- moteur quantitatif → `data/`, `indicators/`, `modules/`, `strategy/`, `backtest/`
- interfaces → `interface/`, `interface_pilotage/`
- exports → `exports/`
- documentation → `docs/`, `documentation_md/`
- tests → `tests/`
- scripts → `scripts/`

---

## ⚙️ 2. Installation

```bash
git clone <url>
cd quant_system
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

---

## ▶️ 3. Lancer le moteur

Le fichier `main.py` est le point d’entrée principal du projet.

Pour l’exécuter :

python main.py

⚠️ Important :  

Si main.py contient du code Streamlit, tu verras un avertissement comme :

Warning: to view this Streamlit app on a browser, run it with: streamlit run main.py

Dans ce cas, lance plutôt :

streamlit run main.py

Cela dépend de ce que contient ton main.py :

si c’est un script Python classique → python main.py

si c’est un dashboard Streamlit → streamlit run main.py

Les deux comportements sont normaux.

## 🧰 Annexes — Commandes utiles

```powershell
cd C:\Users\user\OneDrive\Documents\CODES_CASCADE\quant_system
streamlit run main.py
streamlit run interface/predictability_dashboard.py
streamlit run interface/propfirm_dashboard.py
python scripts/test_scenarios.py
python scripts/check_docs.py
pytest

---

## 🖥️ 4. Lancer un dashboard

Certaines interfaces du projet utilisent Streamlit.  
Elles se trouvent dans le dossier :

interface/

Pour lancer un dashboard réel du projet :

### Exemple 1 — Dashboard de prédictibilité
streamlit run interface/predictability_dashboard.py

### Exemple 2 — Dashboard PropFirm
streamlit run interface/propfirm_dashboard.py

⚠️ Important
Si tu lances un fichier Streamlit avec :
python fichier.py

tu verras apparaître des avertissements comme :
Warning: to view this Streamlit app on a browser, run it with:
streamlit run fichier.py

C’est normal :
→ Streamlit doit être lancé avec streamlit run, pas avec python.

Lancer le menu principal
Ton fichier main.py est un lanceur centralisé.

Pour l’ouvrir :
streamlit run main.py

Il te permet de choisir entre plusieurs modules pédagogiques.

---

## 🧠 5. Explorer le moteur quantitatif (pas à pas)

L’objectif de cette étape est de comprendre comment le moteur fonctionne réellement, en suivant le pipeline dans le code.

### 5.1 Suivre le pipeline dans le code

1. **Ouvrir `main.py`**
   - repérer quelles fonctions sont appelées
   - identifier l’ordre des blocs :
     ```
     data → indicators → modules → strategy → backtest → exports
     ```

2. **Explorer `data/`**
   - ouvrir le fichier principal (ex. `loader.py`)
   - comprendre comment les données sont chargées et validées

3. **Explorer `indicators/`**
   - ouvrir 1 ou 2 indicateurs
   - faire le lien avec `docs/reference/indicator_math.md`

4. **Explorer `modules/quant/`**
   - repérer les modules : structure, volatilité, orderflow, signaux avancés
   - comprendre quels signaux ils produisent

5. **Explorer `strategy/`**
   - identifier où se trouvent :
     - le filtrage
     - la consolidation
     - la décision
     - la gestion du risque
     - le position sizing

6. **Explorer `backtest/`**
   - repérer la boucle principale de simulation
   - faire le lien avec `docs/architecture/diagrams/backtest_timing_diagram.md`

### 5.2 Construire une “trace mentale” du pipeline

En lisant les dossiers **dans cet ordre** :

data/ → indicators/ → modules/quant/ → strategy/ → backtest/ → exports/

Tu dois pouvoir te raconter l’histoire complète :

> “Les données entrent ici, sont transformées là, enrichies ici, donnent des signaux là, la stratégie décide ici, le backtest simule là, puis les résultats partent dans exports/.”

---

## 📚 6. Lire la documentation (parcours guidé)

La documentation du projet est vaste.  
Ce parcours te permet de la lire **dans le bon ordre**, sans te perdre.

### 6.1 Comprendre l’architecture globale

Commencer par :

1. `docs/README.md`  
   → vue d’ensemble de toute la documentation

2. `docs/architecture/README.md`  
   → structure interne du moteur

3. `docs/architecture/diagrams/quant_pipeline_overview.md`  
   → pipeline quantitatif complet

4. `docs/architecture/diagrams/master_map.md`  
   → carte maîtresse du système (vue globale ultime)

Objectif :  
**avoir la carte mentale du système avant d’entrer dans les détails.**

---

### 6.2 Comprendre le moteur quantitatif

Lire ensuite :

1. `docs/quant_engine/README.md`  
   → description du moteur interne

2. `docs/reference/architecture_principles.md`  
   → principes fondamentaux de conception

3. `docs/reference/strategy_design_principles.md`  
   → comment les stratégies sont construites

4. `docs/reference/risk_management_principles.md`  
   → gestion du risque et sizing

Objectif :  
**comprendre comment le moteur pense et décide.**

---

### 6.3 Explorer les détails techniques

Pour aller plus loin :

1. `docs/reference/indicator_math.md`  
   → formules des indicateurs

2. `docs/reference/metrics_definitions.md`  
   → définitions des métriques

3. `docs/reference/data_quality_standards.md`  
   → normes de qualité des données

4. `docs/reference/performance_tuning.md`  
   → optimisation des performances

Objectif :  
**maîtriser les briques techniques et mathématiques.**

---

### 6.4 Utiliser le sommaire global

Pour naviguer rapidement :

docs/TOC.md

Ce fichier liste **toute la documentation**, dossier par dossier.

---

## 🧪 7. Lancer les tests (et comprendre ce qu’ils couvrent)

Les tests permettent de vérifier que le moteur fonctionne correctement après chaque modification.

### 7.1 Lancer tous les tests

Depuis la racine du projet :

pytest

Si tout est correct, tu verras un résumé indiquant que les tests sont passés avec succès.

7.2 Ce que les tests doivent couvrir
Le dossier tests/ doit contenir des tests pour les blocs suivants :

data/ → chargement, nettoyage, validation

indicators/ → calcul des indicateurs

modules/quant/ → signaux avancés

strategy/ → filtrage, décision, gestion du risque

backtest/ → boucle de simulation, métriques

L’objectif est de garantir que chaque brique du moteur fonctionne indépendamment.

7.3 Quand lancer les tests
Toujours :

avant un commit

avant une Pull Request

après une modification importante

après une mise à jour de dépendances

7.4 Si un test échoue
Lire le message d’erreur

Identifier le fichier concerné

Corriger le code

Relancer :

pytest

Répéter jusqu’à obtenir un passage complet.

---

=== SECTION À AJOUTER DANS docs/onboarding.md ===

## 🤝 8. Contribuer au projet (procédure pas à pas)

Cette section décrit **exactement** comment contribuer proprement au projet, sans casser la structure ni introduire d’incohérences.

---

### 8.1 Préparer ton environnement Git

1. Cloner le dépôt (si ce n’est pas déjà fait) :

git clone <url_du_depot>
cd quant_system

Créer une branche dédiée pour ta modification :

git checkout -b feature/nom_fonctionnalite

8.2 Faire une modification propre

Chaque modification doit respecter trois règles :

Modifier le code dans le dossier approprié
(ex. data/, indicators/, modules/quant/, strategy/, etc.)

Mettre à jour la documentation associée
(dans docs/ ou documentation_md/ selon la nature du changement)

Vérifier la cohérence avec :

docs/reference/best_practices.md

docs/reference/architecture_principles.md

8.3 Lancer les tests
Avant de commit :
pytest

Si un test échoue → corriger avant d’aller plus loin

Si tout passe → continuer

8.4 Préparer le commit

Vérifier les fichiers modifiés :
git status

Ajouter les fichiers :
git add <fichiers_modifiés>

Committer avec un message clair :
git commit -m "Ajout de XXX dans YYY"

8.5 Pousser et ouvrir une Pull Request

git push origin feature/nom_fonctionnalite

Puis ouvrir une PR depuis ton remote vers la branche principale.

8.6 Référence
Pour les détails avancés, consulter :

docs/reference/how_to_contribute.md

---

streamlit run main.py

---

## 📜 Licence

Le projet est distribué sous licence **CC BY‑NC‑ND 4.0**.

Cela signifie que :
- vous pouvez lire et exécuter le code pour un usage personnel  
- vous devez citer l’auteur si vous partagez le projet  
- vous ne pouvez pas modifier ou redistribuer une version modifiée  
- vous ne pouvez pas utiliser le projet à des fins commerciales  
