import os

def run_ui_scenario(steps: list):
    print("UI scenario received:", steps)
    return {
        "status": "success",
        "message": "UI sceanrio executed (mock)"
    }

def run_db_scenarios(filename: str):
    path = os.path.join("scenarios", filename)
    if not os.path.exists(path):
        return {
            "status": "error",
            "message": f"Scenario file '{filename}' does not exist"
        }
    return {
        "status": "ok",
        "message": "All scenarios executed (mock)"
    }
