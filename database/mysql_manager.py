from __future__ import annotations

import os
from typing import Any, Dict, List, Optional

import mysql.connector
from mysql.connector import Error

from .db_base import DBManager

class MySQLManager(DBManager):
    """
    Operaciones CRUD para la base de datos MySQL gestionando las tablas:
    `duenos`, `veterinarios`, `animales`, `cuidados` y `alimentos`
    """

    # ──────────────────────────────── Configuración ──────────────────────────────────
    def __init__(
        self,
        host: Optional[str] = None,
        port: Optional[int] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
        database: Optional[str] = None,
    ) -> None:
        """
        Inicializa la configuración de conexión a la base de datos.

        Parameters
        ----------
        host : str, optional
            Dirección del servidor MySQL. Por defecto, variable de entorno DB_HOST o 'localhost'.
        port : int, optional
            Puerto del servidor MySQL. Por defecto, DB_PORT o 3306.
        user : str, optional
            Usuario de la base de datos. Por defecto, DB_USER.
        password : str, optional
            Contraseña de la base de datos. Por defecto, DB_PASS.
        database : str, optional
            Nombre de la base de datos. Por defecto, DB_NAME.

        Raises
        ------
        Error
            Si ocurre un error al conectar o inicializar la base de datos.
        """
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
        """
        Establece y devuelve una nueva conexión MySQL.

        Returns
        -------
        mysql.connector.connection.MySQLConnection
            Conexión activa a la base de datos.

        Raises
        ------
        Error
            Si la conexión falla.
        """
        try:
            return mysql.connector.connect(**self.config)
        except Error as e:
            print(" Error al conectar a MySQL:", e)
            raise

    def _init_db(self) -> None:
        """
        Crea las tablas necesarias si no existen.

        Tablas creadas:
        - duenos
        - veterinarios
        - animales
        - cuidados
        - alimentos

        Raises
        ------
        Error
            Si ocurre un error durante la creación de tablas.
        """
        ddl_duenos = """
        CREATE TABLE IF NOT EXISTS duenos (
            id_dueno      INT AUTO_INCREMENT PRIMARY KEY,
            nif            VARCHAR(20) UNIQUE NOT NULL,
            nombre         VARCHAR(100) NOT NULL,
            direccion      VARCHAR(200) NOT NULL,
            telefono       VARCHAR(20) NOT NULL
        ) ENGINE=InnoDB;
        """
        ddl_veterinarios = """
        CREATE TABLE IF NOT EXISTS veterinarios (
            colegiado_id  INT AUTO_INCREMENT PRIMARY KEY,
            nombre         VARCHAR(100) NOT NULL,
            nif            VARCHAR(20) UNIQUE NOT NULL,
            direccion      VARCHAR(200) NOT NULL,
            telefono       VARCHAR(20) NOT NULL
        ) ENGINE=InnoDB;
        """
        ddl_animales = """
        CREATE TABLE IF NOT EXISTS animales (
            id_animal       INT AUTO_INCREMENT PRIMARY KEY,
            chip            VARCHAR(60) UNIQUE NOT NULL,
            especie         VARCHAR(100) NOT NULL,
            nombre          VARCHAR(100) NOT NULL,
            edad            INT,
            raza            VARCHAR(100),
            dueno_id        INT,
            colegiado_id    INT,
            CONSTRAINT fk_dueno
                FOREIGN KEY (dueno_id)
                REFERENCES duenos(id_dueno),
            CONSTRAINT fk_veterinario
                FOREIGN KEY (colegiado_id)
                REFERENCES veterinarios(colegiado_id)
        ) ENGINE=InnoDB;
        """
        ddl_cuidados = """
        CREATE TABLE IF NOT EXISTS cuidados (
            id        INT AUTO_INCREMENT PRIMARY KEY,
            animal_id VARCHAR(60)      NOT NULL,
            fecha     DATE             NOT NULL,
            tipo      VARCHAR(50)      NOT NULL,
            estado    VARCHAR(20)      NOT NULL DEFAULT 'pendiente',
            notas     TEXT,
            CONSTRAINT fk_animal
                FOREIGN KEY (animal_id)
                REFERENCES animales(chip)
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """
        ddl_alimentos = """
        CREATE TABLE IF NOT EXISTS alimentos (
            id               INT AUTO_INCREMENT PRIMARY KEY,
            tipo_animal      VARCHAR(50)  NOT NULL,
            alimento         VARCHAR(100) NOT NULL,
            cantidad         INT          NOT NULL,
            fecha_caducidad  DATE         NOT NULL,
            coste            FLOAT        NOT NULL
        ) ENGINE=InnoDB;
        """

        with self._connect() as conn:
            cur = conn.cursor()
            try:
                cur.execute(ddl_duenos)
                cur.execute(ddl_veterinarios)
                cur.execute(ddl_animales)
                cur.execute(ddl_cuidados)
                cur.execute(ddl_alimentos)
            finally:
                cur.close()

    # ──────────────────────────────── Dueños ──────────────────────────────────
    def insert_dueno(self, datos: Dict[str, Any]) -> int:
        """
        Inserta un nuevo dueño en la tabla `duenos`.

        Parameters
        ----------
        datos : dict
            Diccionario con las claves:
            - nif (str): NIF del dueño.
            - nombre (str): Nombre del dueño.
            - direccion (str): Dirección del dueño.
            - telefono (str): Teléfono del dueño.

        Returns
        -------
        int
            ID autogenerado `id_dueno`.

        Raises
        ------
        Error
            Si ocurre un error durante la inserción.
        """
        q = (
            "INSERT INTO duenos (nif, nombre, direccion, telefono) "
            "VALUES (%(nif)s, %(nombre)s, %(direccion)s, %(telefono)s)"
        )
        with self._connect() as conn:
            cur = conn.cursor()
            try:
                cur.execute(q, datos)
                return cur.lastrowid
            finally:
                cur.close()

    def get_duenos(self) -> List[Dict[str, Any]]:
        """
        Obtiene todos los registros de la tabla `duenos`.

        Returns
        -------
        List[Dict[str, Any]]
            Lista de diccionarios con los campos:
            `id_dueno`, `nif`, `nombre`, `direccion`, `telefono`.

        Raises
        ------
        Error
            Si ocurre un error durante la consulta.
        """
        q = "SELECT id_dueno, nif, nombre, direccion, telefono FROM duenos"
        with self._connect() as conn:
            cur = conn.cursor(dictionary=True)
            try:
                cur.execute(q)
                return cur.fetchall()
            finally:
                cur.close()
