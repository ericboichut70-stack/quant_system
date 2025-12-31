# 📦 Module 10 — utils/

1 Description générale

Le module utils/ regroupe toutes les fonctions transversales, indépendantes du domaine métier, qui servent de fondation technique au moteur quantitatif.
Il fournit des outils génériques, réutilisables dans l’ensemble du système, notamment :

hashing SHA256

timers

logs simples

helpers divers

fonctions utilitaires pour la manipulation de données

Ce module garantit :

la cohérence technique

la réduction de duplication

la centralisation des outils communs

la traçabilité (via hashing)

2 Responsabilités du module

Le module utils/ doit :

fournir des fonctions utilitaires génériques

offrir un hashing stable et déterministe

proposer des helpers pour le logging, le timing, etc.

rester totalement indépendant des modules métier

Il ne doit pas :

manipuler les signaux

faire du ML

faire de l’optimisation

modifier les données métier

dépendre du pipeline

👉 C’est un module purement technique, transversal et stable.

3 Entrées / sorties

Entrées
Selon les fonctions :

objets Python (dict, DataFrame, listes…)

chaînes de caractères

timestamps

paramètres divers

Sorties
Selon les fonctions :

hash SHA256

logs formatés

mesures de temps

objets transformés

4 Classes / fonctions principales

## Hashing

Fonctions de hashing SHA256 pour garantir la traçabilité.

Méthodes typiques :

compute_hash(obj)  
→ renvoie un hash SHA256 stable

Utilisation :

signature d’un run

auditabilité

versionnage interne

### Helpers

Fonctions utilitaires génériques.

Méthodes typiques :

log(message)  
→ log simple, timestampé

timer(func)  
→ décorateur pour mesurer le temps d’exécution

flatten_dict(d)  
→ aplatissement de dictionnaires

safe_get(d, key, default)  
→ accès sécurisé aux dictionnaires

### DataUtils (optionnel)

Fonctions utilitaires pour manipuler les DataFrames.

Méthodes typiques :

ensure_datetime(df)

ensure_sorted(df)

drop_nan_edges(df)

5 Exemple d’utilisation

from quant_system.utils.hashing import compute_hash
from quant_system.utils.helpers import log, timer

@timer
def compute_something():
    return sum(range(100000))

result = compute_something()
log(f"Résultat : {result}")

hash_value = compute_hash({"result": result})
print("Hash :", hash_value)

6 Dépendances internes

Le module utils/ dépend uniquement de :

hashlib

time

pandas (optionnel)

numpy (optionnel)

Il ne doit jamais dépendre :

des modules métier (signals, features, orderflow, etc.)

du pipeline

de l’optimisation

👉 C’est le module le plus bas dans la hiérarchie des dépendances.

7 Points d’extension (v2 / v3)

v2
logger structuré

gestion avancée des exceptions

outils de profiling

hashing multi‑objets

v3
logger asynchrone

outils de monitoring

intégration avec un dashboard interne

utilitaires pour exécution distribuée
