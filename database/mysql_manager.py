"""
Gestor para MySQL en PythonAnywhere (o cualquier servidor MySQL).
Instala  mysql-connector-python  en tu venv.
"""
import os 
import mysql.connector
from mysql.connector import Error
from typing import Dict, Any, List
from .db_base import DBManager

# --- configura aquí tus credenciales de PythonAnywhere ---
CONFIG = dict(
    host=os.getenv("DB_HOST", "lucasbeneyto.mysql.pythonanywhere-services.com"),
    user=os.getenv("DB_USER", "lucasbeneyto"),
    password=os.getenv("DB_PASSWORD", "Blancamola24"),
    database=os.getenv("DB_NAME", "lucasbeneyto$default"),
)

_ANIMAL_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS animales (
  chip     VARCHAR(60) AUTO_INCREMENT PRIMARY KEY,
  tipo     VARCHAR(20),
  nombre   VARCHAR(100),
  edad     INT,


);
"""

class MySQLManager(DBManager):
    """Gestor concreto para MySQL (PythonAnywhere)."""

    def __init__(self, config: Dict[str, str] | None = None):
        self.config = config or CONFIG
        self._init_db()

    # ---------- helpers ----------
    def _connect(self):
        return mysql.connector.connect(**self.config)

    def _init_db(self):
        with self._connect() as con:
            cur = con.cursor()
            cur.execute(_ANIMAL_TABLE_SQL)
            con.commit()
            cur.close()

    # ---------- implementación CRUD ----------
    def insert_animal(self, datos: Dict[str, Any]) -> int:
        q = ("INSERT INTO animales (tipo, nombre, edad, chip, "
             "VALUES (%(tipo)s, %(nombre)s, %(edad)s, %(chip)s, %(raza)s)")
        with self._connect() as con:
            cur = con.cursor()
            cur.execute(q, datos)
            con.commit()
            last_id = cur.lastrowid
            cur.close()
            return last_id

    def get_animales(self) -> List[Dict[str, Any]]:
        with self._connect() as con:
            cur = con.cursor(dictionary=True)
            cur.execute("SELECT * FROM animales")
            rows = cur.fetchall()
            cur.close()
            return rows

    def update_animal(self, animal_id: int, datos: Dict[str, Any]) -> None:
        sets = ", ".join(f"{k}=%({k})s" for k in datos.keys())
        datos["id"] = animal_id
        q = f"UPDATE animales SET {sets} WHERE id=%(id)s"
        with self._connect() as con:
            cur = con.cursor()
            cur.execute(q, datos)
            con.commit()
            cur.close()

    def delete_animal(self, animal_id: int) -> None:
        with self._connect() as con:
            cur = con.cursor()
            cur.execute("DELETE FROM animales WHERE id=%s", (animal_id,))
            con.commit()
            cur.close()
