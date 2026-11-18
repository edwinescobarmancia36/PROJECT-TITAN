from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter()

@router.get("/sports", tags=["catalog"])
def get_sports():
    """Obtener la lista de deportes disponibles"""
    return [
        {"id": 1, "name": "Football", "code": "football", "country": "Global"},
        {"id": 2, "name": "Basketball", "code": "nba", "country": "USA"}
    ]

@router.get("/teams", tags=["catalog"])
def get_teams(sport: Optional[str] = Query(None, description="Filtrar por deporte (ej. football, nba)")):
    """Obtener el catálogo de equipos filtrado por deporte"""
    teams_db = [
        {"id": 101, "name": "Real Madrid", "sport": "football", "country": "Spain"},
        {"id": 102, "name": "Celta de Vigo", "sport": "football", "country": "Spain"},
        {"id": 103, "name": "PSV Eindhoven", "sport": "football", "country": "Netherlands"},
        {"id": 201, "name": "Los Angeles Lakers", "sport": "nba", "country": "USA"}
    ]
    
    if sport:
        return [t for t in teams_db if t["sport"].lower() == sport.lower()]
    return teams_db
