from fastapi import FastAPI
from .scenarios import router as scenarios_router
from .assets import router as assets_router
from .runner import router as runner_router

def register_routes(app: FastAPI):
    app.include_router(scenarios_router, prefix="/scenarios", tags=["Scenarios"])
    app.include_router(assets_router, prefix="/assets", tags=["Assets"])
    app.include_router(runner_router, prefix="/runner", tags=["Runner"])
