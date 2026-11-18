from fastapi import APIRouter, Query
from typing import Optional, List
from pydantic import BaseModel
from app.domain.schemas import SystemStatus, SportCode

router = APIRouter()

class Team(BaseModel):
    id: int
    name: str
    sport: str
    country: Optional[str] = None

# Nuevo modelo para los partidos / cuotas del Proyecto Titán
class Match(BaseModel):
    id: int
    sport: str
    league: str
    home_team: str
    away_team: str
    odds_1: float
    odds_x: Optional[float] = None
    odds_2: float
    status: str = "upcoming"

TEAMS_DB = [
    {"id": 1, "name": "FC Barcelona", "sport": "football", "country": "Spain"},
    {"id": 2, "name": "Real Madrid", "sport": "football", "country": "Spain"},
    {"id": 3, "name": "FC Motagua", "sport": "football", "country": "Honduras"},
    {"id": 4, "name": "Olimpia", "sport": "football", "country": "Honduras"},
    {"id": 5, "name": "Los Angeles Lakers", "sport": "nba", "country": "USA"},
    {"id": 6, "name": "Chicago Bulls", "sport": "nba", "country": "USA"},
]

# Base de datos simulada de partidos conectada a los deportes
MATCHES_DB = [
    {
        "id": 1,
        "sport": "football",
        "league": "Copa del Rey",
        "home_team": "CD Alcoyano",
        "away_team": "RCD Mallorca",
        "odds_1": 6.50,
        "odds_x": 4.10,
        "odds_2": 1.46
    },
    {
        "id": 2,
        "sport": "football",
        "league": "Segunda División Egipto",
        "home_team": "Pharco FC",
        "away_team": "El Entag El Harby",
        "odds_1": 1.85,
        "odds_x": 3.20,
        "odds_2": 4.30
    },
    {
        "id": 3,
        "sport": "nba",
        "league": "NBA Regular Season",
        "home_team": "Los Angeles Lakers",
        "away_team": "Chicago Bulls",
        "odds_1": 1.72,
        "odds_x": None,
        "odds_2": 2.15
    }
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
    results = TEAMS_DB
    if sport:
        results = [t for t in results if t["sport"].lower() == sport.lower()]
    if search:
        results = [t for t in results if search.lower() in t["name"].lower()]
    return results

# NUEVO ENDPOINT: Para que Streamlit reciba los partidos al filtrar por deporte
@router.get("/matches", response_model=List[Match], tags=["analytics"])
def get_matches(
    sport: Optional[str] = Query(None, description="Filtrar partidos por deporte (ej. football, nba)")
):
    results = MATCHES_DB
    if sport:
        results = [m for m in results if m["sport"].lower() == sport.lower()]
    return results
