import pandas as pd
from typing import Dict, Any, Optional

class TransactionsService:
    """Service pour la consultation et le filtrage des transactions bancaires."""

    @staticmethod
    def get_paginated_transactions(
        df: pd.DataFrame, 
        page: int = 1, 
        limit: int = 10, 
        tx_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Récupère une liste paginée de transactions en gérant les valeurs NaN.
        """
        filtered_df = df
        if tx_type:
            filtered_df = df[df['type'] == tx_type]

        start = (page - 1) * limit
        end = start + limit
        
        # Sélection du subset
        subset_df = filtered_df.iloc[start:end].copy()
        
        # NETTOYAGE CRUCIAL : Remplace les NaN par 0 pour être compatible JSON
        subset_df = subset_df.fillna(0)
        
        # Conversion en liste de dictionnaires
        transactions = subset_df.to_dict(orient="records")
        
        return {
            "page": page,
            "limit": limit,
            "total_results": len(filtered_df),
            "transactions": transactions
        }
    @staticmethod
    def get_unique_types(df: pd.DataFrame) -> list[str]:
        """
        Récupère la liste des types de transactions uniques (Route 4).
        """
        # On récupère les valeurs uniques de la colonne 'type' et on les convertit en liste
        return df['type'].unique().tolist()
    
    @staticmethod
    def get_transactions_by_origin(df: pd.DataFrame, customer_id: str) -> list[dict]:
        """
        Récupère les transactions émises par un client (Route 7).
        """
        # Filtrage sur nameOrig (Source)
        result = df[df['nameOrig'] == customer_id].copy()
        return result.fillna(0).to_dict(orient="records")

    @staticmethod
    def get_transactions_by_destination(df: pd.DataFrame, customer_id: str) -> list[dict]:
        """
        Récupère les transactions reçues par un client (Route 8).
        """
        # Filtrage sur nameDest (Destination)
        result = df[df['nameDest'] == customer_id].copy()
        return result.fillna(0).to_dict(orient="records")