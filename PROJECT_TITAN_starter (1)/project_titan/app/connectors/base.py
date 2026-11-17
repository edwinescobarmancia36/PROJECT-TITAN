from abc import ABC, abstractmethod
from typing import Any

class OddsProvider(ABC):
    """Contrato común. Los adaptadores nunca deben alterar el histórico."""

    provider_name: str

    @abstractmethod
    async def fetch_odds(self, sport_key: str) -> list[dict[str, Any]]:
        raise NotImplementedError
