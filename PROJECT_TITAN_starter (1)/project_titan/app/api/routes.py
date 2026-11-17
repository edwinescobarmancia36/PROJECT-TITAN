from fastapi import APIRouter
from app.domain.schemas import SystemStatus, SportCode

router = APIRouter()

@router.get("/status", response_model=SystemStatus, tags=["system"])
def status():
    return SystemStatus(
        project="PROJECT TITAN",
        status="initializing",
        supported_sports=list(SportCode),
        betting_execution_enabled=False,
    )

@router.get("/sports", tags=["catalog"])
def sports():
    return [{"code": s.value, "name": s.name} for s in SportCode]
