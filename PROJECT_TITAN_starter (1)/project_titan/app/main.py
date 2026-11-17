from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router

app = FastAPI(title=settings.app_name, version="0.1.0")
app.include_router(router, prefix=settings.api_v1_prefix)

@app.get("/", tags=["system"])
def root():
    return {"project": "PROJECT TITAN", "status": "scaffold", "mode": "manual"}

@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}
