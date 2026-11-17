from typing import Any
import httpx
from app.core.config import settings
from app.connectors.base import OddsProvider

class TheOddsAPIConnector(OddsProvider):
    provider_name = "the_odds_api"

    async def fetch_odds(self, sport_key: str) -> list[dict[str, Any]]:
        if not settings.odds_api_key:
            raise RuntimeError("ODDS_API_KEY no está configurada")
        url = f"{settings.odds_api_base_url}/v4/sports/{sport_key}/odds"
        params = {
            "apiKey": settings.odds_api_key,
            "regions": "us,uk,eu,au",
            "markets": "h2h,spreads,totals",
            "oddsFormat": "decimal",
        }
        async with httpx.AsyncClient(timeout=20) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            payload = response.json()
        # Se devuelve payload original para normalización posterior.
        return payload
