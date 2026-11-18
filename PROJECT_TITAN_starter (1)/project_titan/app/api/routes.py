# app/api/routes.py
from fastapi import APIRouter, Query
from typing import Optional, List, Dict, Any
from app.services.sports_service import get_all_sports, get_match_analysis

router = APIRouter()

@router.get("/sports", tags=["catalog"])
def get_sports() -> List[Dict[str, Any]]:
    """Obtener la lista completa de deportes disponibles"""
    return get_all_sports()

@router.get("/matches/analysis", tags=["betting-analytics"])
def get_matches_analysis(
    league: Optional[str] = Query(None, description="Filtrar por liga (ej. La Liga, Eredivisie)")
) -> List[Dict[str, Any]]:
    """Obtener estadísticas avanzadas de partidos (Cuotas 1x2, xG, BTTS, Córners y Forma de últimos 15 partidos)"""
    return get_match_analysis(league=league)
