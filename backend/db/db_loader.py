import sqlite3

def load_scenario_from_db(db_path="scenario.db", base_id=1):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT key, action, wait FROM baseAction WHERE base_id=?", (base_id,))
    base_actions = cur.fetchall()
    if not base_actions:
        raise ValueError(f"base_id {base_id} does not exist")

    base_action_dict = {key: {"action": action, "wait": wait} for key, action, wait in base_actions}

    cur.execute("""
        SELECT key, target, position, wait, threshold, min_match_count, method, action
        FROM scenario WHERE base_id=? ORDER BY id
    """, (base_id,))

    steps = []
    for row in cur.fetchall():
        key, target, position, wait, threshold, min_match_count, method, action = row
        if key not in base_action_dict:
            raise ValueError(f"key '{key}' defined in scenario does not exist in the baseAction.")

        step_action = action if action else base_action_dict[key]["action"]
        step_wait = wait if wait is not None else base_action_dict[key]["wait"]

        steps.append({
            "key": key,
            "action": step_action,
            "wait": step_wait,
            "target": target,
            "position": position,
            "threshold": threshold,
            "min_match_count": min_match_count,
            "method": method
        })

    conn.close()
    return steps
