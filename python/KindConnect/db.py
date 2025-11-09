# db.py
import sqlite3
from typing import List, Dict

DB_NAME = "kindscore.db"


def get_conn():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create tables if they don't exist."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS acts (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            entity      TEXT NOT NULL,
            description TEXT,
            impact      INTEGER NOT NULL,   -- 1-100
            upvotes     INTEGER DEFAULT 0,
            downvotes   INTEGER DEFAULT 0
        );
        """
    )
    conn.commit()
    conn.close()


def add_act(entity: str, description: str, impact: int) -> int:
    """Insert a new act and return its id."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO acts (entity, description, impact) VALUES (?, ?, ?)",
        (entity, description, impact),
    )
    conn.commit()
    act_id = cur.lastrowid
    conn.close()
    return act_id


def vote_on_act(act_id: int, up: bool):
    """Increment upvote or downvote."""
    conn = get_conn()
    cur = conn.cursor()
    field = "upvotes" if up else "downvotes"
    cur.execute(f"UPDATE acts SET {field} = {field} + 1 WHERE id = ?", (act_id,))
    conn.commit()
    conn.close()


def get_act(act_id: int) -> Dict:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM acts WHERE id = ?", (act_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return {}
    return _row_to_dict(row)


def get_all_acts() -> List[Dict]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM acts ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return [_row_to_dict(r) for r in rows]


def _row_to_dict(row: sqlite3.Row) -> Dict:
    net = max(row["upvotes"] - row["downvotes"], 0)
    kind_score = round(row["impact"] * (1 + net / 10.0))
    return {
        "id": row["id"],
        "entity": row["entity"],
        "description": row["description"],
        "impact": row["impact"],
        "upvotes": row["upvotes"],
        "downvotes": row["downvotes"],
        "net_votes": net,
        "kind_score": kind_score,
    }
