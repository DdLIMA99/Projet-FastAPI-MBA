# 🏦 Banking Transactions API - MBA ESG

## 📝 Présentation du Projet
Cette API industrielle a été développée pour traiter et analyser un volume massif de transactions bancaires (**+13 millions de lignes**, ~1.2 Go) avec une latence de réponse optimisée.

Le projet intègre une **fusion de données dynamique** entre des transactions brutes (CSV) et des labels de fraude (JSON) pour permettre une analyse de sécurité en temps réel.

---

## 🏗️ Architecture des Services
L'application respecte une architecture modulaire découpée en **5 services spécialisés** :

| Service | Rôle Principal |
| :--- | :--- |
| **`system_service.py`** | Diagnostic, état de santé et gestion du chargement/fusion des datasets. |
| **`transactions_service.py`** | Moteur de recherche, pagination et filtrage multi-critères. |
| **`stats_service.py`** | Calcul des agrégations globales et statistiques descriptives. |
| **`fraud_detection_service.py`** | Analyse des risques et détection des incidents de fraude. |
| **`customer_service.py`** | Agrégation des données et historique par identifiant client. |

---

## 🚀 Installation et Lancement

### 1. Prérequis
* Python 3.10+
* Dossier `data/` contenant : `transactions_data.csv` et `train_fraud_labels.json`.

### 2. Installation des dépendances
```bash
pip install fastapi uvicorn pandas
3. Démarrage de l'API
Bash

uvicorn src.banking_api.main:app --reload
🛠️ Points d'entrée principaux (Endpoints)
Accédez à la documentation interactive (Swagger UI) sur : http://127.0.0.1:8000/docs.

Santé du système : GET /api/system/health

Transactions : GET /api/transactions?page=1&limit=10

Détails Transaction : GET /api/transactions/{tx_id}

Résumé Fraude : GET /api/fraud/summary

Stats Client : GET /api/customers/{client_id}/stats

📊 Performance & Validation
Volume de données : 13 305 915 lignes traitées.

Optimisation : Temps de réponse ultra-rapide grâce au pré-chargement en mémoire (Singleton Pattern).

Fiabilité : Gestion robuste des valeurs manquantes (NaN) et correction de la sérialisation JSON pour les colonnes complexes comme zip.

Sécurité : Intégration réussie des labels de fraude convertis en indicateurs numériques.