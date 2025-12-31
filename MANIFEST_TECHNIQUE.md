# 📜 MANIFESTE TECHNIQUE — quant_system

(Document maître — Version 1.0.0)

Résumé exécutif
quant_system est un moteur quantitatif modulaire, extensible et auditable, conçu pour analyser les marchés financiers, extraire des signaux robustes et préparer l’intégration future de modèles de machine learning.
Ce manifeste décrit :

l’architecture complète du système,

les modules, leurs responsabilités et leurs flux,

les conventions de conception,

l’héritage historique du TRADING_BOT,

les principes fondamentaux,

le glossaire,

les annexes techniques.

Ce document constitue la référence centrale pour tout développement présent et futur.

Table des matières

1 Résumé exécutif

2 Historique : TRADING_BOT
2.1 Données d’entrée standard

2.2 Chaîne de traitement recommandée

2.3 Conventions de codage

2.4 Version stabilisée (20 décembre 2025)

3 Architecture moderne : quant_system
3.1 Vision générale

3.2 Architecture globale

3.3 Modules

3.3.1 data/

3.3.2 indicators/

3.3.3 structure/

3.3.4 orderflow/

3.3.5 features/

3.3.6 signals/

3.3.7 attribution/

3.3.8 optimization/

3.3.9 utils/

3.3.10 pipeline/

3.4 Flux de données

3.5 Règles de conception

3.6 Conventions de nommage

3.7 Conventions de code

3.8 Tests

3.9 Documentation

3.10 Roadmap

4 Principes fondamentaux

5 Glossaire

6 Annexes
6.1 Diagramme d’architecture global (UML + Flux + Dépendances)
6.1.1 UML global — Architecture statique

+-------------------------------------------------------------+
|                         quant_system                        |
+-------------------------------------------------------------+
|                                                             |
|  +------------------+      +-----------------------------+  |
|  |      data/       | ---> |         indicators/         |  |
|  +------------------+      +-----------------------------+  |
|            |                          |                    |
|            v                          v                    |
|  +------------------+      +-----------------------------+  |
|  |    structure/    | ---> |         orderflow/          |  |
|  +------------------+      +-----------------------------+  |
|            |                          |                    |
|            v                          v                    |
|  +-------------------------------------------------------+ |
|  |                      features/                        | |
|  +-------------------------------------------------------+ |
|                              |                             |
|                              v                             |
|  +------------------+      +-----------------------------+  |
|  |     signals/     | ---> |        attribution/         |  |
|  +------------------+      +-----------------------------+  |
|                              |                             |
|                              v                             |
|                     +---------------------+                |
|                     |    optimization/    |                |
|                     +---------------------+                |
|                                                             |
|  +-------------------------------------------------------+ |
|  |                       pipeline/                       | |
|  +-------------------------------------------------------+ |
|                                                             |
|  +------------------+                                      |
|  |      utils/      |  (transversal, sans dépendances)     |
|  +------------------+                                      |
+-------------------------------------------------------------+

6.1.2 Diagramme de flux — Pipeline dynamique

┌──────────────┐
│    data/     │  Chargement, nettoyage, normalisation
└───────┬──────┘
        │
        ▼
┌──────────────┐
│ indicators/  │  EMA, ADX, volatilité
└───────┬──────┘
        │
        ▼
┌──────────────┐
│ structure/   │  Swings, HH/HL/LH/LL, ZigZag
└───────┬──────┘
        │
        ▼
┌──────────────┐
│ orderflow/   │  Delta, imbalance, absorption
└───────┬──────┘
        │
        ▼
┌──────────────┐
│  features/   │  Construction des features multi‑niveaux
└───────┬──────┘
        │
        ▼
┌──────────────┐
│  signals/    │  Génération des signaux + scoring
└───────┬──────┘
        │
        ▼
┌──────────────┐
│ attribution/ │  Analyse post‑signal, contributions
└───────┬──────┘
        │
        ▼
┌──────────────┐
│ optimization/│  Recherche de paramètres
└──────────────┘

        │
        ▼
┌──────────────┐
│  pipeline/   │  Orchestration complète
└──────────────┘

utils/ → utilisé partout, sans dépendances inverses

6.1.3 Diagramme des dépendances — Hiérarchie logique

utils/
   ↑
   │ (utilisé par tous, dépend de personne)
   │
data/
   ↑
   │
indicators/
   ↑
   │
structure/
   ↑
   │
orderflow/
   ↑
   │
features/
   ↑
   │
signals/
   ↑
   │
attribution/
   ↑
   │
optimization/
   ↑
   │
pipeline/

Règles clés :

Aucune dépendance descendante n’est autorisée.

utils/ est la base technique.

pipeline/ est le sommet orchestral.

Chaque module ne dépend que des modules situés au-dessus de lui dans la hiérarchie.

6.2 Diagramme de flux

6.3 Diagramme des dépendances

6.4 Conventions de versionnage

6.5 Conventions de commit

2 Historique : TRADING_BOT
2.1 Données d’entrée standard
(Ton contenu existant est intégré ici, inchangé.)

2.2 Chaîne de traitement recommandée
(Ton contenu existant est intégré ici, inchangé.)

2.3 Conventions de codage
(Ton contenu existant est intégré ici, inchangé.)

2.4 Version stabilisée (20 décembre 2025)
(Ton contenu existant est intégré ici, inchangé.)

3 Architecture moderne : quant_system
3.1 Vision générale
quant_system est un moteur quantitatif modulaire conçu pour :

analyser les marchés financiers,

extraire des signaux robustes,

préparer l’intégration future du ML,

garantir la reproductibilité et l’auditabilité.

3.2 Architecture globale
Flux ascendant :
data → indicators → structure → orderflow → features → signals → attribution → optimization

Le pipeline orchestre l’ensemble.

3.3 Modules
Chaque module est documenté dans docs/modules/.

3.3.1 data/
Chargement, nettoyage, normalisation.

3.3.2 indicators/
EMA, ADX, volatilité, primitives analytiques.

3.3.3 structure/
Swings, HH/HL/LH/LL, ZigZag.

3.3.4 orderflow/
Delta, imbalance, absorption.

3.3.5 features/
Construction de features multi‑niveaux.

3.3.6 signals/
Génération de signaux, scoring.

3.3.7 attribution/
Analyse post‑signal, contributions.

3.3.8 optimization/
Recherche de paramètres.

3.3.9 utils/
Hashing, logs, helpers.

3.3.10 pipeline/
Orchestration complète.

3.4 Flux de données
(Texte déjà fourni dans le manifeste modulaire.)

3.5 Règles de conception
modularité

flux unidirectionnel

pureté fonctionnelle

traçabilité

extensibilité

3.6 Conventions de nommage
(Texte déjà fourni.)

3.7 Conventions de code
(Texte déjà fourni.)

3.8 Tests
(Texte déjà fourni.)

3.9 Documentation
(Texte déjà fourni.)

3.10 Roadmap
(Texte déjà fourni.)

4 Principes fondamentaux
Clarté : chaque module a une responsabilité unique.

Auditabilité : chaque run est traçable via SHA256.

Modularité : tout composant est remplaçable.

Extensibilité : architecture pensée pour le ML futur.

Reproductibilité : aucun effet de bord, flux déterministe.

Transmission : documentation complète, stable, durable.

5 Glossaire
OHLCV : Open, High, Low, Close, Volume

Delta : pression acheteurs vs vendeurs

Imbalance : déséquilibre directionnel

Swing : point haut/bas significatif

ZigZag : filtre structurel

Feature : variable explicative

Signal : décision binaire ou directionnelle

Attribution : explication du signal

Pipeline : orchestrateur du système

6 Annexes
6.1 Diagramme d’architecture global
(sera ajouté après génération)

6.2 Diagramme de flux
(sera ajouté après génération)

6.3 Diagramme des dépendances
(sera ajouté après génération)

6.4 Conventions de versionnage
SemVer : MAJOR.MINOR.PATCH

6.5 Conventions de commit
feat:

fix:

docs:

refactor:

test:

chore:
