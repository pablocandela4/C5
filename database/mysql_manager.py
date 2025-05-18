"""
mysql_manager.py

Gestor concreto para MySQL/MariaDB.

Requisitos:
    pip install mysql-connector-python
"""

from __future__ import annotations

import os
from typing import Any, Dict, List, Optional

import mysql.connector
from mysql.connector import Error

from .db_base import DBManager


class MySQLManager(DBManager):
    """
    Implementa los métodos CRUD definidos en DBManager para MySQL.
    Gestiona dos tablas: `animales` y `cuidados`.
    """

    # ──────────────────────────────── Setup ──────────────────────────────────
    def __init__(
        self,
        host: str | None = None,
        port: int | None = None,
        user: str | None = None,
        password: str | None = None,
        database: str | None = None,
    ) -> None:
        # Config desde argumentos o variables de entorno
        self.config: Dict[str, Any] = {
            "host": host or os.getenv("DB_HOST", "localhost"),
            "port": port or int(os.getenv("DB_PORT", 3306)),
            "user": user or os.getenv("DB_USER", ""),
            "password": password or os.getenv("DB_PASS", ""),
            "database": database or os.getenv("DB_NAME", ""),
            "autocommit": True,
        }
        self._init_db()

    def _connect(self):
        """Devuelve una conexión nueva usando self.config."""
        try:
            return mysql.connector.connect(**self.config)
        except Error as e:
            print("❌ Error al conectar a MySQL:", e)
            raise

    def _init_db(self) -> None:
        """Crea tablas `animales` y `cuidados` si no existen."""
        ddl_animales = """
        CREATE TABLE IF NOT EXISTS animales (
            chip     INT AUTO_INCREMENT PRIMARY KEY,
            tipo     VARCHAR(20)  NOT NULL,
            nombre   VARCHAR(100) NOT NULL,
            raza     VARCHAR(100),
            edad     INT
        ) ENGINE=InnoDB;
        """

        ddl_cuidados = """
        CREATE TABLE IF NOT EXISTS cuidados (
            id        INT AUTO_INCREMENT PRIMARY KEY,
            animal_id INT          NOT NULL,
            fecha     DATE         NOT NULL,
            tipo      VARCHAR(50)  NOT NULL,
            estado    VARCHAR(20)  NOT NULL DEFAULT 'pendiente',
            notas     TEXT,
            CONSTRAINT fk_animal
                FOREIGN KEY (animal_id)
                REFERENCES animales(chip)
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """

        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute(ddl_animales)
            cur.execute(ddl_cuidados)
            cur.close()

    # ───────────────────────────── Animales ──────────────────────────────────
    def insert_animal(self, datos: Dict[str, Any]) -> int:
        """
        Espera keys: tipo, nombre, edad (opcional), raza (opcional).
        Devuelve el chip autogenerado.
        """
        q = """
        INSERT INTO animales (tipo, nombre, raza, edad)
        VALUES (%(tipo)s, %(nombre)s, %(raza)s, %(edad)s)
        """
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute(q, datos)
            animal_id = cur.lastrowid
            cur.close()
            return animal_id

    def get_animales(self) -> List[Dict[str, Any]]:
        q = "SELECT * FROM animales"
        with self._connect() as conn:
            cur = conn.cursor(dictionary=True)
            cur.execute(q)
            rows = cur.fetchall()
            cur.close()
            return rows

    def update_animal(self, animal_id: int, datos: Dict[str, Any]) -> None:
        if not datos:
            return
        sets = ", ".join(f"{k} = %({k})s" for k in datos.keys())
        datos["chip"] = animal_id
        q = f"UPDATE animales SET {sets} WHERE chip = %(chip)s"
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute(q, datos)
            cur.close()

    def delete_animal(self, animal_id: int) -> None:
        q = "DELETE FROM animales WHERE chip = %s"
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute(q, (animal_id,))
            cur.close()

    # ───────────────────────────── Cuidados ──────────────────────────────────
    def insert_cuidado(self, datos: Dict[str, Any]) -> int:
        """
        Keys obligatorias: animal_id, fecha(YYYY-MM-DD), tipo.
        Keys opcionales: estado, notas.
        """
        q = """
        INSERT INTO cuidados (animal_id, fecha, tipo, estado, notas)
        VALUES (%(animal_id)s, %(fecha)s, %(tipo)s,
                %(estado)s, %(notas)s)
        """
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute(q, datos)
            cuidado_id = cur.lastrowid
            cur.close()
            return cuidado_id

    def get_cuidados(
        self,
        animal_id: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        if animal_id is None:
            q = "SELECT * FROM cuidados ORDER BY fecha DESC"
            params: tuple = ()
        else:
            q = "SELECT * FROM cuidados WHERE animal_id = %s ORDER BY fecha DESC"
            params = (animal_id,)

        with self._connect() as conn:
            cur = conn.cursor(dictionary=True)
            cur.execute(q, params)
            rows = cur.fetchall()
            cur.close()
            return rows

    def update_cuidado(self, cuidado_id: int, datos: Dict[str, Any]) -> None:
        if not datos:
            return
        sets = ", ".join(f"{k} = %({k})s" for k in datos.keys())
        datos["id"] = cuidado_id
        q = f"UPDATE cuidados SET {sets} WHERE id = %(id)s"
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute(q, datos)
            cur.close()

    def delete_cuidado(self, cuidado_id: int) -> None:
        q = "DELETE FROM cuidados WHERE id = %s"
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute(q, (cuidado_id,))
            cur.close()
