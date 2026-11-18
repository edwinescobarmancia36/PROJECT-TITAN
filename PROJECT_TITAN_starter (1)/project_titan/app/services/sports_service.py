# app/services/sports_service.py
from typing import List, Dict, Any, Optional

SPORTS_CATALOG = [
    {"id": 1, "name": "Football", "code": "football", "country": "Global"},
    {"id": 2, "name": "Basketball (NBA)", "code": "nba", "country": "USA"},
    {"id": 3, "name": "Baseball (MLB)", "code": "mlb", "country": "USA"},
    {"id": 4, "name": "American Football (NFL)", "code": "nfl", "country": "USA"},
    {"id": 5, "name": "Ice Hockey (NHL)", "code": "nhl", "country": "USA/Canada"}
]

TEAMS_CATALOG = [
    # --- Football (Fútbol / Soccer) ---
    {"id": 101, "name": "Real Madrid", "sport": "football", "league": "La Liga", "country": "Spain"},
    {"id": 102, "name": "Celta de Vigo", "sport": "football", "league": "La Liga", "country": "Spain"},
    {"id": 103, "name": "FC Barcelona", "sport": "football", "league": "La Liga", "country": "Spain"},
    {"id": 104, "name": "PSV Eindhoven", "sport": "football", "league": "Eredivisie", "country": "Netherlands"},
    {"id": 105, "name": "FC Motagua", "sport": "football", "league": "Liga Nacional", "country": "Honduras"},

    # --- NBA ---
    {"id": 201, "name": "Los Angeles Lakers", "sport": "nba", "league": "NBA", "country": "USA"},
    {"id": 202, "name": "Golden State Warriors", "sport": "nba", "league": "NBA", "country": "USA"},
    {"id": 203, "name": "Boston Celtics", "sport": "nba", "league": "NBA", "country": "USA"},

    # --- MLB ---
    {"id": 301, "name": "New York Yankees", "sport": "mlb", "league": "MLB", "country": "USA"},
    {"id": 302, "name": "Los Angeles Dodgers", "sport": "mlb", "league": "MLB", "country": "USA"},

    # --- NFL ---
    {"id": 401, "name": "Kansas City Chiefs", "sport": "nfl", "league": "NFL", "country": "USA"},
    {"id": 402, "name": "Dallas Cowboys", "sport": "nfl", "league": "NFL", "country": "USA"},

    # --- NHL ---
    {"id": 501, "name": "Edmonton Oilers", "sport": "nhl", "league": "NHL", "country": "Canada"},
    {"id": 502, "name": "Boston Bruins", "sport": "nhl", "league": "NHL", "country": "USA"}
]

def get_all_sports() -> List[Dict[str, Any]]:
    """Devuelve la lista completa de deportes soportados."""
    return SPORTS_CATALOG

def get_all_teams(sport_query: Optional[str] = None, league_query: Optional[str] = None) -> List[Dict[str, Any]]:
    """Devuelve el catálogo de equipos filtrado opcionalmente por deporte o liga."""
    teams = TEAMS_CATALOG
    
    if sport_query:
        s_query = sport_query.lower()
        if s_query in ["futbol", "fútbol"]:
            s_query = "football"
        teams = [t for t in teams if t["sport"].lower() == s_query]
        
    if league_query:
        l_query = league_query.lower()
        teams = [t for t in teams if l_query in t["league"].lower()]
        
    return teams
