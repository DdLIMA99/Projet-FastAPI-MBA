from fastapi import FastAPI, Query, HTTPException
from contextlib import asynccontextmanager
from typing import List, Optional
from .services.stats_service import StatsService

# Imports de tes services [cite: 137, 141]
from .services.system_service import SystemService
from .services.transactions_service import TransactionsService

# Import de tes nouveaux modèles de typage [cite: 166]
from .models.transaction import Transaction, TransactionPaginated
from .services.stats_service import StatsService
from .services.customer_service import CustomerService 
from .services.fraud_detection_service import FraudDetectionService  
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Performance : Chargement unique du dataset de 1.2Go [cite: 143]
    print("Chargement du dataset en cours...")
    SystemService.load_dataset()
    print("Dataset chargé et prêt !")
    yield

app = FastAPI(
    title="Banking Transactions API",
    version="1.0.0",
    description="API REST complète pour les données de transactions bancaires [cite: 35, 42]",
    lifespan=lifespan
)

# --- ROUTES ADMINISTRATION ---

@app.get("/api/system/health")
def health_check() -> dict:
    """Route 19 : Vérifie l'état de santé de l'API (ping, dataset)[cite: 130, 131]."""
    return SystemService.get_health_status()

# --- ROUTES TRANSACTIONS ---

@app.get("/api/transactions", response_model=TransactionPaginated)
def get_transactions(
    page: int = Query(1, ge=1), 
    limit: int = Query(10, le=100), 
    type: Optional[str] = None
):
    """
    Route 1 : Liste paginée des transactions[cite: 52, 53].
    """
    try:
        df = SystemService.get_data()
        return TransactionsService.get_paginated_transactions(df, page=page, limit=limit, tx_type=type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/transactions/types", response_model=List[str])
def get_transaction_types():
    """Route 4 : Liste des types de transactions disponibles[cite: 65, 66]."""
    df = SystemService.get_data()
    return TransactionsService.get_unique_types(df)

@app.get("/api/transactions/{tx_id}", response_model=Transaction)
def get_transaction_details(tx_id: int):
    """Route 2 : Détails d'une transaction par son identifiant[cite: 58, 59]."""
    df = SystemService.get_data()
    result = TransactionsService.get_transaction_by_id(df, tx_id)
    
    if result is None:
        raise HTTPException(status_code=404, detail="Transaction non trouvée")
    return result

@app.get("/api/transactions/by-customer/{customer_id}", response_model=List[Transaction])
def get_customer_sent_transactions(customer_id: str):
    """
    Route 7 : Liste des transactions associées à un client (origine)[cite: 71].
    """
    df = SystemService.get_data()
    return TransactionsService.get_transactions_by_origin(df, customer_id)

@app.get("/api/transactions/to-customer/{customer_id}", response_model=List[Transaction])
def get_customer_received_transactions(customer_id: str):
    """
    Route 8 : Liste des transactions reçues par un client (destination)[cite: 73].
    """
    df = SystemService.get_data()
    return TransactionsService.get_transactions_by_destination(df, customer_id)

@app.get("/api/stats/overview")
def get_stats_overview() -> dict:
    """
    Route 9 : Statistiques globales du dataset.
    """
    df = SystemService.get_data()
    return StatsService.get_overview(df)

@app.get("/api/customers/{client_id}/stats")
def get_client_stats(client_id: int):
    """Route 8 : Statistiques de consommation d'un client."""
    df = SystemService.get_data()
    return CustomerService.get_customer_metrics(df, client_id)

@app.get("/api/customers/{client_id}/transactions")
def get_client_transactions(client_id: int):
    """Route 7 : Historique complet d'un client."""
    df = SystemService.get_data()
    return CustomerService.get_customer_history(df, client_id)

@app.get("/api/fraud/summary")
def get_fraud_report():
    """Route 13 : Résumé de la fraude détectée."""
    df = SystemService.get_data()
    return FraudDetectionService.get_fraud_summary(df)

@app.get("/api/fraud/latest")
def get_recent_frauds(limit: int = 5):
    """Route 14 : Liste des dernières transactions suspectes."""
    df = SystemService.get_data()
    return FraudDetectionService.get_latest_frauds(df, limit)