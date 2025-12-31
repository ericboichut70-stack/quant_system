# 🔐 Security Guidelines — Bonnes Pratiques de Sécurité

Ce document décrit les règles de sécurité à respecter pour garantir l’intégrité du moteur quantitatif, des données, des interfaces et des exports.

---

## 🧭 1. Sécurité du Code

- éviter les imports dynamiques non contrôlés  
- ne jamais exécuter du code externe non vérifié  
- utiliser des environnements virtuels isolés  
- éviter les dépendances obsolètes  
- vérifier les signatures des packages  

---

## 🧱 2. Sécurité des Données

- ne jamais stocker de données sensibles en clair  
- nettoyer les données avant export  
- éviter les fuites d’informations dans les logs  
- vérifier les formats avant ingestion  

---

## 🧪 3. Sécurité des Interfaces

## Dashboards

- ne jamais exposer des fichiers internes  
- limiter les actions utilisateur  
- éviter les injections via paramètres  

## CLI

- valider les entrées utilisateur  
- éviter les commandes dangereuses  
- journaliser les actions critiques  

---

## 📤 4. Sécurité des Exports

- vérifier les chemins d’écriture  
- éviter les noms de fichiers dynamiques non contrôlés  
- ne jamais écraser un fichier sans confirmation  
- nettoyer les données avant export  

---

## 🧬 5. Sécurité du Backtest & de la Stratégie

- vérifier les limites de position  
- éviter les tailles de position invalides  
- contrôler les valeurs extrêmes  
- journaliser les erreurs critiques  

---

## 🧩 6. Sécurité du Déploiement

- utiliser des clés API sécurisées  
- ne jamais versionner des secrets  
- utiliser `.env` pour les variables sensibles  
- limiter les permissions des services externes  
