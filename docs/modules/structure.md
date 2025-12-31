# 📦 Module 4 — structure/

1 Description générale

Le module structure/ est responsable de l’analyse de la structure de marché, un pilier fondamental de ton moteur quantitatif. Il permet d’identifier :

les swings (hauts/bas significatifs)

les points HH / HL / LH / LL

les retournements structurels

les phases directionnelles

les zones de rupture ou de continuation

Ce module fournit une lecture objective, normalisée et réplicable de la structure du prix, indispensable pour :

la génération de signaux

la construction de features

l’analyse de tendance

la validation de conditions multi‑modules

2 Responsabilités du module

Le module structure/ doit :

détecter les swings (hauts/bas significatifs)

classifier les points en HH / HL / LH / LL

produire une structure directionnelle exploitable

fournir un ZigZag simplifié pour lisser le bruit

renvoyer des colonnes propres, alignées sur les données

Il ne doit pas :

générer des signaux

interpréter la tendance (c’est le rôle des indicateurs)

faire de l’orderflow

produire des features

👉 C’est un module d’analyse structurelle pure.

3 Entrées / sorties

Entrées
un DataFrame OHLC propre

paramètres optionnels :

seuil de swing

profondeur minimale

sensibilité du ZigZag

Sorties
Un DataFrame contenant :

swing_high / swing_low

structure (HH, HL, LH, LL)

zigzag (points filtrés)

direction (optionnel : up / down / neutral)

4 Classes / fonctions principales

## SwingDetector

Détecte les swings significatifs.

Méthodes typiques :

detect(data) → renvoie swing_high / swing_low

### ZigZag

Filtre le bruit et simplifie la structure.

Méthodes typiques :

compute(data, threshold) → renvoie une série ZigZag propre

### StructureClassifier

Classe les points en HH / HL / LH / LL.

Méthodes typiques :

classify(swings) → renvoie une colonne structure

5 Exemple d’utilisation

from quant_system.structure.swings import SwingDetector
from quant_system.structure.zigzag import ZigZag
from quant_system.structure.classifier import StructureClassifier

swings = SwingDetector.detect(df)
zigzag = ZigZag.compute(df, threshold=0.02)
structure = StructureClassifier.classify(swings)

df["swing_high"] = swings["high"]
df["swing_low"] = swings["low"]
df["zigzag"] = zigzag
df["structure"] = structure

6 Dépendances internes

Le module structure/ dépend uniquement de :

pandas

numpy

Il peut utiliser les indicateurs (EMA, ADX) en lecture seule, mais ne doit pas :

modifier les données

dépendre du module signals

dépendre du module features

👉 Le flux doit rester data → indicators → structure → orderflow → features → signals.

7 Points d’extension (v2 / v3)

v2
structure multi‑timeframes

détection automatique de régimes structurels

classification ML des swings

structure fractale

v3
structure adaptative (ZigZag dynamique)

structure basée sur volatilité réalisée

structure multi‑actifs

structure en temps réel
