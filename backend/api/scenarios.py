from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from services.scenario_service import list_scenarios, save_scenario, delete_scenario, load_scenario, rename_scenario

router = APIRouter()

class SaveRequest(BaseModel):
    name: str
    steps: list

class LoadRequest(BaseModel):
    filename: str

class DeleteRequest(BaseModel):
    filename: str

class RenameRequest(BaseModel):
    old: str
    new: str

@router.get("/list")
def list_scenarios_api():
    return {"scenarios": list_scenarios()}

@router.post("/save")
def save_scenario_api(req: SaveRequest):
    return save_scenario(req.name, req.steps)

@router.post("/load")
def load_scenario_api(req: LoadRequest):
    return load_scenario(req.filename)

@router.post("/delete")
def delete_scenario_api(req: DeleteRequest):
    return delete_scenario(req.filename)

@router.post("/rename")
def rename_scenario_api(req: RenameRequest):
    return rename_scenario(req.old, req.new)
