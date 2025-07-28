from fastapi import APIRouter, Request
from services.runner_service import run_ui_scenario, run_db_scenario, run_all_scenarios

router = APIRouter()

@router.post("/run-ui")
async def run_ui(request: Request):
    steps = await request.json()
    return run_ui_scenario(steps)

@router.post("/run")
def run_scenario_api(data: dict):
    filename = data.get("filename")
    return run_db_scenario(filename)

@router.post("/run-all")
def run_all_api():
    return run_all_scenarios()
