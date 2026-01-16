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

2. Installation des dépendances
Exécutez la commande suivante pour installer les bibliothèques nécessaires : pip install fastapi uvicorn pandas

3. Démarrage de l'API
Lancez le serveur avec cette commande : uvicorn src.banking_api.main:app --reload

🛠️ Points d'entrée principaux (Endpoints)
Une fois le serveur lancé, vous pouvez consulter la documentation interactive Swagger UI à l'adresse suivante : http://127.0.0.1:8000/docs

Voici les routes principales à tester :

Santé du système : GET /api/system/health

Liste des Transactions : GET /api/transactions

Détails d'une Transaction : GET /api/transactions/{tx_id}

Résumé de la Fraude : GET /api/fraud/summary

Statistiques Client : GET /api/customers/{client_id}/stats

📊 Performance & Validation
Volume : 13 305 915 lignes traitées avec succès.

Optimisation : Temps de réponse rapide grâce au pré-chargement en mémoire (Singleton Pattern).

Fiabilité : Correction de la sérialisation JSON pour les données manquantes (NaN), notamment sur la colonne zip.