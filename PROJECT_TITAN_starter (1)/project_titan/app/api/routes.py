from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from pydantic import BaseModel
from app.domain.schemas import SystemStatus, SportCode

router = APIRouter()

# Modelo de ejemplo para los equipos
class Team(BaseModel):
    id: int
    name: str
    sport: str
    country: Optional[str] = None

# Base de datos simulada de equipos para tu análisis de apuestas
TEAMS_DB = [
    {"id": 1, "name": "FC Barcelona", "sport": "football", "country": "Spain"},
    {"id": 2, "name": "Real Madrid", "sport": "football", "country": "Spain"},
    {"id": 3, "name": "FC Motagua", "sport": "football", "country": "Honduras"},
    {"id": 4, "name": "Olimpia", "sport": "football", "country": "Honduras"},
    {"id": 5, "name": "Los Angeles Lakers", "sport": "nba", "country": "USA"},
    {"id": 6, "name": "Chicago Bulls", "sport": "nba", "country": "USA"},
]

@router.get("/status", response_model=SystemStatus, tags=["system"])
def status():
    return SystemStatus(
        project="PROJECT TITAN",
        status="active",
        supported_sports=list(SportCode),
        betting_execution_enabled=False,
    )

@router.get("/sports", tags=["catalog"])
def sports():
    return [{"code": s.value, "name": s.name} for s in SportCode]

@router.get("/teams", response_model=List[Team], tags=["catalog"])
def get_teams(
    sport: Optional[str] = Query(None, description="Filtrar por deporte (ej. football, nba)"),
    search: Optional[str] = Query(None, description="Buscar por nombre de equipo")
):
    """
    Permite consultar equipos específicos con filtros opcionales por deporte o nombre.
    """
    results = TEAMS_DB
    
    if sport:
        results = [t for t in results if t["sport"].lower() == sport.lower()]
        
    if search:
        results = [t for t in results if search.lower() in t["name"].lower()]
        
    return results
