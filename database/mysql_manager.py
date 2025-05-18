"""
Gestor concreto para MySQL.
Instala mysql-connector-python en tu venv:
    pip install mysql-connector-python
"""

import os
import mysql.connector
from mysql.connector import Error
from typing import Dict, Any, List, Optional
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
            print(" Error al conectar a MySQL:", e)
            raise


def _init_db(self) -> None:
    """
    Inicializa la base de datos creando las tablas si no existen.
    """
    try:
        with self._connect() as con:
            cur = con.cursor()


            cur.execute("""
                   CREATE TABLE IF NOT EXISTS duenos (
                       id_dueno INT AUTO_INCREMENT PRIMARY KEY,
                       nif VARCHAR(20) UNIQUE NOT NULL,
                       nombre VARCHAR(100) NOT NULL,
                       direccion VARCHAR(200) NOT NULL,
                       telefono VARCHAR(20) NOT NULL
                   )
               """)

            cur.execute("""
                   CREATE TABLE IF NOT EXISTS veterinarios (
                       colegiado_id INT AUTO_INCREMENT PRIMARY KEY,
                       nombre VARCHAR(100) NOT NULL,
                       nif VARCHAR(20) UNIQUE NOT NULL,
                       direccion VARCHAR(200) NOT NULL,
                       telefono VARCHAR(20) NOT NULL
                   )
               """)


            cur.execute("""
                   CREATE TABLE IF NOT EXISTS animales (
                       id_animal INT AUTO_INCREMENT PRIMARY KEY,
                       chip VARCHAR(60) UNIQUE NOT NULL,
                       especie VARCHAR(100) NOT NULL,
                       nombre VARCHAR(100) NOT NULL,
                       edad INT,
                       raza VARCHAR(100),
                       dueno_id INT,
                       veterinario_id INT,
                       FOREIGN KEY (dueno_id) REFERENCES duenos(id_dueno),
                       FOREIGN KEY (veterinario_id) REFERENCES veterinarios(colegiado_id)
                   )
               """)

            con.commit()
            cur.close()
    except Error as e:
        print(f"Error al inicializar la base de datos: {e}")
        raise  # Relanza la excepción


def insertar_animal(self, datos: Dict[str, Any]) -> int:
    """
    Inserta un nuevo animal en la base de datos.

    Parameters
    ----------
    datos : Dict[str, Any]
        Diccionario con los datos del animal a insertar.
        Debe contener las claves: 'especie', 'nombre', 'chip'.
        Puede contener opcionalmente: 'edad', 'raza', 'dueno_id', 'veterinario_id'.

    Returns
    -------
    int
        El ID del animal insertado.

    Raises
    ------
    Exception
        Si ocurre un error durante la inserción.
    """
    try:
        q = ("INSERT INTO animales (chip, especie, nombre, edad, raza, dueno_id, veterinario_id) "
             "VALUES (%(chip)s, %(especie)s, %(nombre)s, %(edad)s, %(raza)s, %(dueno_id)s, %(veterinario_id)s)")
        with self._connect() as con:
            cur = con.cursor()
            cur.execute(q, datos)
            con.commit()
            last_id = cur.lastrowid
            cur.close()
            return last_id
    except Error as e:
        print(f"Error al insertar animal: {e}")
        raise  # Relanza la excepción


def obtener_animales(self) -> List[Dict[str, Any]]:
    """
    Obtiene todos los animales de la base de datos.

    Returns
    -------
    List[Dict[str, Any]]
        Una lista de diccionarios, donde cada diccionario representa un animal.
        Las claves de cada diccionario son: 'id_animal', 'chip', 'especie', 'nombre', 'edad', 'raza', 'dueno_id', 'veterinario_id'.
        Si no hay animales, devuelve una lista vacía.

    Raises
    ------
    Exception
        Si ocurre un error durante la consulta.
    """
    try:
        with self._connect() as con:
            cur = con.cursor(dictionary=True)
            cur.execute(
                "SELECT id_animal, chip, especie, nombre, edad, raza, dueno_id, veterinario_id FROM animales")
            rows = cur.fetchall()
            cur.close()
            return rows
    except Error as e:
        print(f"Error al obtener animales: {e}")
        raise  # Relanza la excepción


def obtener_animal(self, animal_id: int) -> Optional[Dict[str, Any]]:
    """
    Obtiene un animal por su ID.

    Parameters
    ----------
    animal_id : int
        ID del animal a obtener.

    Returns
    -------
    Optional[Dict[str, Any]]
        Un diccionario representando al animal si se encuentra, None si no.
        Devuelve None si no se encuentra ningún animal con el ID dado.

    Raises
    ------
    Exception
        Si ocurre un error durante la consulta.
    """
    try:
        with self._connect() as con:
            cur = con.cursor(dictionary=True)
            cur.execute(
                "SELECT id_animal, chip, especie, nombre, edad, raza, dueno_id, veterinario_id FROM animales WHERE id_animal = %s",
                (animal_id,),
            )
            row = cur.fetchone()
            cur.close()
            return row  # Devuelve None si no se encuentra el animal
    except Error as e:
        print(f"Error al obtener animal: {e}")
        raise  # Relanza la excepción


def actualizar_animal(self, animal_id: int, datos: Dict[str, Any]) -> None:
    """
    Actualiza la información de un animal existente.

    Parameters
    ----------
    animal_id : int
        ID del animal a actualizar.
    datos : Dict[str, Any]
        Diccionario con los datos a actualizar.  Puede contener cualquier
        combinación de las claves: 'especie', 'nombre', 'edad', 'raza', 'chip', 'dueno_id', 'veterinario_id'.

    Raises
    ------
    Exception
        Si ocurre un error durante la actualización.
    """
    try:
        sets = ", ".join(f"{k} = %({k})s" for k in datos.keys())
        datos["id_animal"] = animal_id  # Asegúrate de que el ID esté en los datos
        q = f"UPDATE animales SET {sets} WHERE id_animal = %(id_animal)s"
        with self._connect() as con:
            cur = con.cursor()
            cur.execute(q, datos)
            con.commit()
            cur.close()
        # No es necesario devolver nada en caso de éxito, por eso es None
    except Error as e:
        print(f"Error al actualizar animal: {e}")
        raise  # Relanza la excepción


def eliminar_animal(self, animal_id: int) -> None:
    """
    Elimina un animal de la base de datos.

    Parameters
    ----------
    animal_id : int
        ID del animal a eliminar.

    Raises
    ------
    Exception
        Si ocurre un error durante la eliminación.
    """
    try:
        with self._connect() as con:
            cur = con.cursor()
            cur.execute("DELETE FROM animales WHERE id_animal = %s", (animal_id,))
            con.commit()
            cur.close()
    except Error as e:
        print(f"Error al eliminar animal: {e}")
        raise  # Relanza la excepción


def insertar_dueno(self, datos: Dict[str, Any]) -> int:
    """
    Inserta un nuevo dueño en la base de datos.

    Parameters
    ----------
    datos : Dict[str, Any]
        Diccionario con los datos del dueño a insertar.
        Debe contener las claves: 'nombre', 'nif', 'direccion', 'telefono'.

    Returns
    -------
    int
        El ID del dueño insertado.

    Raises
    ------
    Exception
        Si ocurre un error durante la inserción.
    """
    try:
        q = ("INSERT INTO duenos (nif, nombre, direccion, telefono) "
             "VALUES (%(nif)s, %(nombre)s, %(direccion)s, %(telefono)s)")
        with self._connect() as con:
            cur = con.cursor()
            cur.execute(q, datos)
            con.commit()
            last_id = cur.lastrowid
            cur.close()
            return last_id
    except Error as e:
        print(f"Error al insertar dueño: {e}")
        raise  # Relanza la excepción


def obtener_duenos(self) -> List[Dict[str, Any]]:
    """
    Obtiene todos los dueños de la base de datos.

    Returns
    -------
    List[Dict[str, Any]]
        Una lista de diccionarios, donde cada diccionario representa un dueño.
        Las claves de cada diccionario son: 'id_dueno', 'nif', 'nombre', 'direccion', 'telefono'.
        Si no hay dueños, devuelve una lista vacía.

    Raises
    ------
    Exception
        Si ocurre un error durante la consulta.
    """
    try:
        with self._connect() as con:
            cur = con.cursor(dictionary=True)
            cur.execute("SELECT id_dueno, nif, nombre, direccion, telefono FROM duenos")
            rows = cur.fetchall()
            cur.close()
            return rows
    except Error as e:
        print(f"Error al obtener dueños: {e}")
        raise  # Relanza la excepción


def obtener_dueno(self, dueno_id: int) -> Optional[Dict[str, Any]]:
    """
    Obtiene un dueño por su ID.

    Parameters
    ----------
    dueno_id : int
        ID del dueño a obtener.

    Returns
    -------
    Optional[Dict[str, Any]]
        Un diccionario representando al dueño si se encuentra, None si no.
        Devuelve None si no se encuentra ningún dueño con el ID dado.

    Raises
    ------
    Exception
        Si ocurre un error durante la consulta.
    """
    try:
        with self._connect() as con:
            cur = con.cursor(dictionary=True)
            cur.execute("SELECT id_dueno, nif, nombre, direccion, telefono FROM duenos WHERE id_dueno = %s",
                        (dueno_id,))
            row = cur.fetchone()
            cur.close()
            return row  # Devuelve None si no se encuentra el dueño
    except Error as e:
        print(f"Error al obtener dueno: {e}")
        raise  # Relanza la excepción


def actualizar_dueno(self, dueno_id: int, datos: Dict[str, Any]) -> None:
    """
    Actualiza la información de un dueño existente.

    Parameters
    ----------
    dueno_id : int
        ID del dueño a actualizar.
    datos : Dict[str, Any]
        Diccionario con los datos a actualizar.  Puede contener cualquier
        combinación de las claves: 'nombre', 'nif', 'direccion', 'telefono'.

    Raises
    ------
    Exception
        Si ocurre un error durante la actualización.
    """
    try:
        sets = ", ".join(f"{k} = %({k})s" for k in datos.keys())
        datos["id_dueno"] = dueno_id
        q = f"UPDATE duenos SET {sets} WHERE id_dueno = %(id_dueno)s"
        with self._connect() as con:
            cur = con.cursor()
            cur.execute(q, datos)
            con.commit()
            cur.close()
    except Error as e:
        print(f"Error al actualizar dueño: {e}")
        raise  # Relanza la excepción


def eliminar_dueno(self, dueno_id: int) -> None:
    """
    Elimina un dueño de la base de datos.

    Parameters
    ----------
    dueno_id : int
        ID del dueño a eliminar.

    Raises
    ------
    Exception
        Si ocurre un error durante la eliminación.
    """
    try:
        with self._connect() as con:
            cur = con.cursor()
            cur.execute("DELETE FROM duenos WHERE id_dueno = %s", (dueno_id,))
            con.commit()
            cur.close()
    except Error as e:
        print(f"Error al eliminar dueño: {e}")
        raise  # Relanza la excepción


def insertar_veterinario(self, datos: Dict[str, Any]) -> int:
    """
    Inserta un nuevo veterinario en la base de datos.

    Parameters
    ----------
    datos : Dict[str, Any]
        Diccionario con los datos del veterinario a insertar.
        Debe contener las claves: 'nombre', 'colegiado_id'.
        Puede contener opcionalmente: 'nif', 'direccion', 'telefono'.

    Returns
    -------
    int
        El ID del veterinario insertado.

    Raises
    ------
    Exception
        Si ocurre un error durante la inserción.
    """
    try:
        q = ("INSERT INTO veterinarios (nombre, nif, direccion, telefono, colegiado_id) "
             "VALUES (%(nombre)s, %(nif)s, %(direccion)s, %(telefono)s, %(colegiado_id)s)")
        with self._connect() as con:
            cur = con.cursor()
            cur.execute(q, datos)
            con.commit()
            last_id = cur.lastrowid
            cur.close()
            return last_id
    except Error as e:
        print(f"Error al insertar veterinario: {e}")
        raise  # Relanza la excepción


def obtener_veterinarios(self) -> List[Dict[str, Any]]:
    """
    Obtiene todos los veterinarios de la base de datos.

    Returns
    -------
    List[Dict[str, Any]]
        Una lista de diccionarios, donde cada diccionario representa un veterinario.
        Las claves del diccionario son: 'colegiado_id', 'nombre', 'nif', 'direccion', 'telefono'.
        Si no hay veterinarios, devuelve una lista vacía.

    Raises
    ------
    Exception
        Si ocurre un error durante la consulta.
    """
    try:
        with self._connect() as con:
            cur = con.cursor(dictionary=True)
            cur.execute("SELECT colegiado_id, nombre, nif, direccion, telefono FROM veterinarios")
            rows = cur.fetchall()
            cur.close()
            return rows
    except Error as e:
        print(f"Error al obtener veterinarios: {e}")
        raise  # Relanza la excepción


def obtener_veterinario(self, colegiado_id: int) -> Optional[Dict[str, Any]]:
    """
    Obtiene un veterinario por su ID de colegiado.

    Parameters
    ----------
    colegiado_id : int
        ID de colegiado del veterinario a obtener.

    Returns
    -------
    Optional[Dict[str, Any]]
        Un diccionario representando al veterinario si se encuentra, None si no.
        Devuelve None si no se encuentra ningún veterinario con el ID dado.

    Raises
    ------
    Exception
        Si ocurre un error durante la consulta.
    """
    try:
        with self._connect() as con:
            cur = con.cursor(dictionary=True)
            cur.execute(
                "SELECT colegiado_id, nombre, nif, direccion, telefono FROM veterinarios WHERE colegiado_id = %s",
                (colegiado_id,))
            row = cur.fetchone()
            cur.close()
            return row  # Devuelve None si no se encuentra el veterinario
    except Error as e:
        print(f"Error al obtener veterinario: {e}")
        raise  # Relanza la excepción


def actualizar_veterinario(self, colegiado_id: int, datos: Dict[str, Any]) -> None:
    """
    Actualiza la información de un veterinario existente.

    Parameters
    ----------
    colegiado_id : int
        ID del veterinario a actualizar (colegiado_id).
    datos : Dict[str, Any]
        Diccionario con los datos a actualizar.  Puede contener cualquier
        combinación de las claves: 'nombre', 'nif', 'direccion', 'telefono', 'colegiado_id'.

    Raises
    ------
    Exception
        Si ocurre un error durante la actualización.
    """
    try:
        sets = ", ".join(f"{k} = %({k})s" for k in datos.keys())
        datos["colegiado_id"] = colegiado_id
        q = f"UPDATE veterinarios SET {sets} WHERE colegiado_id = %(colegiado_id)s"
        with self._connect() as con:
            cur = con.cursor()
            cur.execute(q, datos)
            con.commit()
            cur.close()
    except Error as e:
        print(f"Error al actualizar veterinario: {e}")
        raise  # Relanza la excepción


def eliminar_veterinario(self, colegiado_id: int) -> None:
    """
    Elimina un veterinario de la base de datos.

    Parameters
    ----------
    colegiado_id : int
        ID del veterinario a eliminar (colegiado_id).

    Raises
    ------
    Exception
        Si ocurre un error durante la eliminación.
    """
    try:
        with self._connect() as con:
            cur = con.cursor()
            cur.execute("DELETE FROM veterinarios WHERE colegiado_id = %s", (colegiado_id,))
            con.commit()
            cur.close()
    except Error as e:
        print(f"Error al eliminar veterinario: {e}")
        raise  # Relanza la excepción
