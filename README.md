🏦 Banking Transactions API - MBA ESG
📝 Présentation du Projet
Cette API industrielle a été développée pour traiter et analyser un volume massif de transactions bancaires (+13 millions de lignes, ~1.2 Go) avec une latence de réponse inférieure à 500ms.

Le projet intègre une fusion de données entre des transactions brutes (CSV) et des labels de fraude (JSON) pour permettre une analyse de sécurité en temps réel.

🏗️ Architecture des Services
Conformément aux spécifications, l'application est découpée en 5 services internes spécialisés :

system_service.py : Diagnostic, état de santé de l'API et gestion du chargement/fusion des datasets.

transactions_service.py : Moteur de recherche, pagination et filtrage multi-critères des transactions.

stats_service.py : Calcul des agrégations globales et statistiques descriptives.

fraud_detection_service.py : Analyse des risques, scoring et détection des incidents de fraude.

customer_service.py : Agrégation des données et historique par identifiant client.

🚀 Installation et Lancement
1. Prérequis
Python 3.10+

Dossier data/ contenant les fichiers : transactions_data.csv et train_fraud_labels.json.

2. Installation des dépendances
Bash

pip install fastapi uvicorn pandas
3. Démarrage de l'API
Bash

uvicorn src.banking_api.main:app --reload
🛠️ Points d'entrée principaux (Endpoints)
Une fois l'API lancée, accédez à la documentation interactive sur : http://127.0.0.1:8000/docs

Santé du système : GET /api/system/health

Transactions (Route 1) : GET /api/transactions?page=1&limit=10

Résumé Fraude (Route 13) : GET /api/fraud/summary

Stats Client (Route 8) : GET /api/customers/{client_id}/stats

📊 Performance & Validation
Dataset : 13 305 915 lignes traitées.

Temps de réponse : < 500ms grâce au pré-chargement en mémoire (Singleton Pattern).

Sécurité : Intégration réussie des labels de fraude textuels ("Yes"/"No") convertis en booléens pour le calcul du risque