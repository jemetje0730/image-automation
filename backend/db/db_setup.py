import os
import sqlite3

def pos_to_str(pos):
    if isinstance(pos, list):
        return ",".join(map(str, pos))
    return pos

def create_db_with_scenarios(db_path, steps):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS baseAction (
            base_id INTEGER NOT NULL,
            key TEXT NOT NULL,
            action TEXT NOT NULL,
            wait REAL DEFAULT 0.5,
            PRIMARY KEY (base_id, key)
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS scenario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            base_id INTEGER NOT NULL,
            key TEXT NOT NULL,
            action TEXT,
            target TEXT NOT NULL,
            position TEXT,
            wait REAL,
            threshold REAL,
            min_match_count INTEGER,
            method TEXT,
            FOREIGN KEY (base_id) REFERENCES baseAction(base_id)
        )
    """)

    cur.execute("INSERT OR IGNORE INTO baseAction (base_id, key, action, wait) VALUES (1, 'A', 'click', 0.5)")
    cur.execute("INSERT OR IGNORE INTO baseAction (base_id, key, action, wait) VALUES (1, 'R', 'screen', 0.5)")

    for step in steps:
        if step.get("action") == "next":
            continue
        cur.execute("""
            INSERT INTO scenario (
                base_id, key, action, target, position,
                wait, threshold, min_match_count, method
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            1,
            "R" if step["action"] == "screen" else "A",
            step.get("action"),
            step.get("target"),
            pos_to_str(step.get("position")),
            step.get("wait", 0.5),
            step.get("threshold"),
            step.get("min_match_count"),
            step.get("method"),
        ))

    conn.commit()
    conn.close()

def add_scenario_to_db(db_path, base_id, base_actions=None, steps=[]):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    if base_actions:
        for base_action in base_actions:
            cur.execute("""
                INSERT OR IGNORE INTO baseAction (base_id, key, action, wait)
                VALUES (?, ?, ?, ?)
            """, (
                base_id,
                base_action.get("key"),
                base_action.get("action"),
                base_action.get("wait", 0.5)
            ))

    for step in steps:
        cur.execute("""
            INSERT INTO scenario (
                base_id, key, action, target, position, wait,
                threshold, min_match_count, method
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            base_id,
            step.get("key"),
            step.get("action"),
            step.get("target"),
            step.get("position"),
            step.get("wait", 0.5),
            step.get("threshold"),
            step.get("min_match_count"),
            step.get("method")
        ))

    conn.commit()
    conn.close()

def delete_scenario_steps_from_db(db_path, base_id):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("DELETE FROM scenario WHERE base_id = ?", (base_id,))
    conn.commit()
    conn.close()
    print(f"base_id={base_id} deleted")
