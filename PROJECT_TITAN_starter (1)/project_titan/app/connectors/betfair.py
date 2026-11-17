from app.connectors.base import OddsProvider

class BetfairExchangeConnector(OddsProvider):
    provider_name = "betfair_exchange"

    async def fetch_odds(self, sport_key: str) -> list[dict]:
        """Pendiente: implementar con credenciales/API autorizadas de Betfair.

        Este adaptador debe conservar back/lay, profundidad, volumen,
        moneda, comisión aplicable y timestamp. No simular precios ni liquidez.
        """
        raise NotImplementedError("Conector Betfair pendiente de credenciales y especificación.")
