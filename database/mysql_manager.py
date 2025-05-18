"""
Gestor concreto para MySQL.
Instala mysql-connector-python en tu venv:
    pip install mysql-connector-python
"""

import os
import mysql.connector
from mysql.connector import Error
from typing import Dict, Any, List
from .db_base import DBManager

class MySQLManager(DBManager):
    """Gestor para MySQL (local o PythonAnywhere)."""

    def __init__(
        self,
        host: str | None = None,
        port: int | None = None,
        user: str | None = None,
        password: str | None = None,
        database: str | None = None,
    ):
        # Carga valores desde .env si no se pasan en el constructor
        self.config = {
            'host': host or os.getenv("DB_HOST", "localhost"),
            'port': port or int(os.getenv("DB_PORT", 3306)),
            'user': user or os.getenv("DB_USER", ""),
            'password': password or os.getenv("DB_PASS", ""),
            'database': database or os.getenv("DB_NAME", ""),
        }
        self._init_db()

    def _connect(self):
        try:
            return mysql.connector.connect(**self.config)
        except Error as e:
            print("❌ Error al conectar a MySQL:", e)
            raise

    def _init_db(self):
        """Crea la tabla 'animales' si no existe."""
        ddl = """
        CREATE TABLE IF NOT EXISTS animales (
            chip     INT AUTO_INCREMENT PRIMARY KEY,
            tipo     VARCHAR(20)  NOT NULL,
            nombre   VARCHAR(100) NOT NULL,
            especie  VARCHAR(100) NOT NULL,
            edad     INT          NOT NULL
        );
        """
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(ddl)
        conn.commit()
        cur.close()
        conn.close()

    # ---------- CRUD Animales ----------

    def insert_animal(self, datos: Dict[str, Any]) -> int:
        q = """
        INSERT INTO animales (tipo, nombre, especie, edad)
        VALUES (%(tipo)s, %(nombre)s, %(especie)s, %(edad)s)
        """
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(q, datos)
        conn.commit()
        last_id = cur.lastrowid
        cur.close()
        conn.close()
        return last_id

    def get_animales(self) -> List[Dict[str, Any]]:
        q = "SELECT * FROM animales"
        conn = self._connect()
        cur = conn.cursor(dictionary=True)
        cur.execute(q)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    def update_animal(self, animal_id: int, datos: Dict[str, Any]) -> None:
        sets = ", ".join(f"{k} = %({k})s" for k in datos.keys())
        datos["chip"] = animal_id
        q = f"UPDATE animales SET {sets} WHERE chip = %(chip)s"
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(q, datos)
        conn.commit()
        cur.close()
        conn.close()

    def delete_animal(self, animal_id: int) -> None:
        q = "DELETE FROM animales WHERE chip = %s"
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(q, (animal_id,))
        conn.commit()
        cur.close()
        conn.close()
