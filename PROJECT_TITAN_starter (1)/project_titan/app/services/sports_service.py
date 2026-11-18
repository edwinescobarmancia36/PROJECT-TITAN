# app/services/sports_service.py
from typing import List, Dict, Any, Optional

SPORTS_CATALOG = [
    {"id": 1, "name": "Football", "code": "football", "country": "Global"},
    {"id": 2, "name": "Basketball (NBA)", "code": "nba", "country": "USA"},
    {"id": 3, "name": "Baseball (MLB)", "code": "mlb", "country": "USA"},
    {"id": 4, "name": "American Football (NFL)", "code": "nfl", "country": "USA"},
    {"id": 5, "name": "Ice Hockey (NHL)", "code": "nhl", "country": "USA/Canada"}
]

# Base de datos simulada de partidos con estadísticas avanzadas para apuestas
MATCHES_STATS_DB = [
    {
        "match_id": 1001,
        "league": "La Liga",
        "home_team": "Real Madrid",
        "away_team": "Celta de Vigo",
        "odds_1x2": {"home": 1.35, "draw": 5.20, "away": 8.50},
        "expected_goals": {"home_xg": 2.45, "away_xg": 0.92},
        "btts": {"yes_prob": 0.58, "no_prob": 0.42},
        "corners_avg": {"home": 6.8, "away": 3.5},
        "recent_form_last_15": {
            "home": "WWWDWWWDWWLLWWW", # Últimos 15 partidos (W=Win, D=Draw, L=Loss)
            "away": "WLDWDLLWWWDLLWD"
        }
    },
    {
        "match_id": 1002,
        "league": "Eredivisie",
        "home_team": "PSV Eindhoven",
        "away_team": "FC Motagua", # Ejemplo internacional simulado
        "odds_1x2": {"home": 1.45, "draw": 4.50, "away": 6.00},
        "expected_goals": {"home_xg": 2.10, "away_xg": 1.15},
        "btts": {"yes_prob": 0.65, "no_prob": 0.35},
        "corners_avg": {"home": 7.2, "away": 4.1},
        "recent_form_last_15": {
            "home": "WWWWLDWWWWWDWWL",
            "away": "WDWWLWDWWWDWLLW"
        }
    }
]

def get_all_sports() -> List[Dict[str, Any]]:
    return SPORTS_CATALOG

def get_match_analysis(league: Optional[str] = None) -> List[Dict[str, Any]]:
    """Devuelve las estadísticas detalladas y cuotas de partidos para análisis de apuestas."""
    matches = MATCHES_STATS_DB
    if league:
        l_query = league.lower()
        matches = [m for m in matches if l_query in m["league"].lower()]
    return matches
