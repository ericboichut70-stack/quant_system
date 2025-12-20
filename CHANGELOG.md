# Changelog — TRADING_BOT

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

## [1.0.0] — 2025-12-20

### Ajouté

- Manifest technique complet (`MANIFEST_TECHNIQUE.md`)
- Diagramme d’architecture (`ARCHITECTURE.md`)
- Pipeline end‑to‑end (`pipeline_demo.py`)
- Script d’audit automatique (`generate_audit.ps1`)
- Note de clôture officielle dans `audit_notes.md`

### Modifié

- Tous les modules du dossier `modules/` ont été corrigés :
  - docstrings complètes
  - suppression du code exécuté au niveau global
  - normalisation des signatures de fonctions
  - ajout de fonctions `summarize_*` lorsque pertinent
  - nettoyage des imports
  - cohérence inter‑modules assurée

### Corrigé

- Import circulaires potentiels
- Docstrings vides
- Commentaires orphelins
- Modules incomplets ou non testés

### Statut

✅ Version stable  
✅ Auditée  
✅ Documentée  
✅ Prête pour extension ou exploitation
