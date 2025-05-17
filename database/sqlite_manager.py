"""
Gestor concreto para SQLite (modo local/desarrollo).
El archivo se crea en  datos/clinica.db  si no existe.
"""
import sqlite3
from pathlib import Path
from typing import Dict, Any, List
from .db_base import DBManager

DB_FILE = Path(__file__).parent.parent / "datos" / "clinica.db"
DB_FILE.parent.mkdir(exist_ok=True)

_ANIMAL_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS animales (
  id       INTEGER PRIMARY KEY AUTOINCREMENT,
  tipo     TEXT NOT NULL,
  nombre   TEXT NOT NULL,
  edad     INTEGER,
  chip     TEXT,
  raza     TEXT
);
"""

class SQLiteManager(DBManager):
    """Gestor concreto para SQLite (uso local)."""

    def __init__(self, db_path: str | Path = DB_FILE):
        self.db_path = str(db_path or DB_FILE)
        self._init_db()

    # ---------- helpers ----------
    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        with self._connect() as con:
            con.execute(_ANIMAL_TABLE_SQL)
            con.commit()

    # ---------- implementación CRUD ----------
    def insert_animal(self, datos: Dict[str, Any]) -> int:
        q = ("INSERT INTO animales (tipo, nombre, edad, chip, raza) "
             "VALUES (:tipo, :nombre, :edad, :chip, :raza)")
        with self._connect() as con:
            cur = con.execute(q, datos)
            con.commit()
            return cur.lastrowid

    def get_animales(self) -> List[Dict[str, Any]]:
        with self._connect() as con:
            cur = con.execute("SELECT * FROM animales")
            cols = [c[0] for c in cur.description]
            return [dict(zip(cols, row)) for row in cur.fetchall()]

    def update_animal(self, animal_id: int, datos: Dict[str, Any]) -> None:
        sets = ", ".join(f"{k}=:{k}" for k in datos.keys())
        datos["id"] = animal_id
        q = f"UPDATE animales SET {sets} WHERE id=:id"
        with self._connect() as con:
            con.execute(q, datos)
            con.commit()

    def delete_animal(self, animal_id: int) -> None:
        with self._connect() as con:
            con.execute("DELETE FROM animales WHERE id=?", (animal_id,))
            con.commit()
