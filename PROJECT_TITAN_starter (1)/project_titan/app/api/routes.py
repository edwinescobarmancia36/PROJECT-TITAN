# app/api/routes.py
from fastapi import APIRouter, Query
from typing import Optional, List, Dict, Any
from app.services.sports_service import get_all_sports, get_all_teams

router = APIRouter()

@router.get("/sports", tags=["catalog"])
def get_sports() -> List[Dict[str, Any]]:
    """Obtener la lista completa de deportes disponibles"""
    return get_all_sports()

@router.get("/teams", tags=["catalog"])
def get_teams(
    sport: Optional[str] = Query(None, description="Filtrar por deporte (ej. football, nba, mlb, nfl, nhl)"),
    league: Optional[str] = Query(None, description="Filtrar por liga (ej. La Liga, NBA, MLB, NFL, NHL)")
) -> List[Dict[str, Any]]:
    """Obtener el catálogo completo de equipos filtrado por deporte o liga"""
    return get_all_teams(sport_query=sport, league_query=league)
