def list_scenarios():
    return ["1_login.db", "2_logout.db"]

def save_scenario(name: str, steps: list):
    # DB save logic
    return {"status": "saved", "db": f"{name}.db"}

def load_scenario(filename: str):
    # DB loading
    return {"status": "loaded", "steps": [...]}
