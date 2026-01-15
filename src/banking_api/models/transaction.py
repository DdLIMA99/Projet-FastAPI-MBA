from pydantic import BaseModel
from typing import List

class Transaction(BaseModel):
    """
    Modèle représentant une transaction bancaire (Format NumPyDoc).
    """
    step: int
    type: str
    amount: float
    nameOrig: str
    oldbalanceOrg: float
    newbalanceOrig: float
    nameDest: str
    oldbalanceDest: float
    newbalanceDest: float
    isFraud: int
    isFlaggedFraud: int

class TransactionPaginated(BaseModel):
    """
    Modèle pour la réponse paginée de la Route 1.
    """
    page: int
    limit: int
    total_results: int
    transactions: List[Transaction]