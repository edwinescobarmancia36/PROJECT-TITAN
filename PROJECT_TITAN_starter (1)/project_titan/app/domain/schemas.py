from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class SportCode(str, Enum):
    FOOTBALL = "football"
    NFL = "nfl"
    NBA = "nba"
    TENNIS = "tennis"
    MLB = "mlb"
    NHL = "nhl"

class SystemStatus(BaseModel):
    project: str
    status: str
    supported_sports: list[SportCode]
    betting_execution_enabled: bool = False

class OddsSnapshot(BaseModel):
    provider: str
    event_id: str
    market_key: str
    selection_key: str
    odds_decimal: float
    captured_at: datetime
    market_type: str  # sportsbook | exchange
    currency: str | None = None
