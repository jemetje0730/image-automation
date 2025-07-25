from fastapi import APIRouter

router = APIRouter()

@router.get("/nodes")
def get_nodes():
    return {"nodes": []} # dummy 