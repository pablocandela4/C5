"""
Clase base que define la interfaz mínima que deberán seguir
los gestores concretos (SQLite y MySQL). También carga .env
y expone la factoría para obtener el gestor correcto.
"""

import os
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from dotenv import load_dotenv

# 1) Carga de variables de entorno
load_dotenv()

print("DB_TYPE=",      os.getenv("DB_TYPE"))
print("DB_USER=",      os.getenv("DB_USER"))
print("DB_PASS=",      os.getenv("DB_PASS"))

DB_TYPE = os.getenv("DB_TYPE", "sqlite")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_NAME = os.getenv("DB_NAME", "datos/clinica.db")
DB_USER = os.getenv("DB_USER", "")
DB_PASS = os.getenv("DB_PASS", "")


# 2) Define la interfaz base
class DBManager(ABC):
    """Interfaz CRUD genérica."""

    @abstractmethod
    def insert_animal(self, datos: Dict[str, Any]) -> int: ...
    @abstractmethod
    def get_animales(self) -> List[Dict[str, Any]]: ...
    @abstractmethod
    def update_animal(self, animal_id: int, datos: Dict[str, Any]) -> None: ...
    @abstractmethod
    def delete_animal(self, animal_id: int) -> None: ...

    # ---------- Alimentos ----------
    @abstractmethod
    def insertar_alimento(self, datos: Dict[str, Any]) -> int:
        """
        Inserta un nuevo alimento en la base de datos.
        Parameters
        ----------
        datos : Dict[str, Any]
            Diccionario con los datos del alimento a insertar.
            Debe contener las claves: 'tipo_animal', 'alimento', 'cantidad', 'fecha_caducidad', 'coste'.
        Returns
        -------
        int
            El ID del alimento insertado.
        Raises
        ------
        Exception
            Si ocurre un error durante la inserción.
        """
        pass

    @abstractmethod
    def obtener_alimentos(self) -> List[Dict[str, Any]]:
        """
        Obtiene todos los alimentos de la base de datos.
        Returns
        -------
        List[Dict[str, Any]]
            Una lista de diccionarios, donde cada diccionario representa un alimento.
            Las claves de cada diccionario son: 'id', 'tipo_animal', 'alimento', 'cantidad', 'fecha_caducidad', 'coste'.
            Si no hay alimentos, devuelve una lista vacía.
        Raises
        ------
        Exception
            Si ocurre un error durante la consulta.
        """
        pass

    @abstractmethod
    def obtener_alimento(self, alimento_id: int) -> Optional[Dict[str, Any]]:
        """
        Obtiene un alimento por su ID.
        Parameters
        ----------
        alimento_id : int
            El id del alimento.
        Returns
        -------
        Optional[Dict[str, Any]]
            Un diccionario representando al alimento si se encuentra, None si no.
        """
        pass

    @abstractmethod
    def actualizar_alimento(self, alimento_id: int, datos: Dict[str, Any]) -> None:
        """
        Actualiza la información de un alimento existente.
        Parameters
        ----------
        alimento_id : int
            ID del alimento a actualizar.
        datos : Dict[str, Any]
            Diccionario con los datos a actualizar. Puede contener cualquier combinación
            de las claves: 'tipo_animal', 'alimento', 'cantidad', 'fecha_caducidad', 'coste'.
        Raises
        ------
        Exception
            Si el alimento no existe o si ocurre un error durante la actualización.
        """
        pass

    @abstractmethod
    def eliminar_alimento(self, alimento_id: int) -> None:
        """
        Elimina un alimento de la base de datos.
        Parameters
        ----------
        alimento_id : int
            ID del alimento a eliminar.
        Raises
        ------
        Exception
            Si el alimento no existe o si ocurre un error durante la eliminación.
        """
        pass


# 3) Importa los gestores concretos *después* de definir DBManager
from .mysql_manager import MySQLManager


# 4) La factoría que escoge el gestor según DB_TYPE
def get_db_manager() -> DBManager:
    """
    Devuelve una instancia de SQLiteManager o MySQLManager según .env.
    """
    if DB_TYPE.lower() == "mysql":
        return MySQLManager(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
    # Ruta al archivo, si DB_NAME es la ruta relativa al .db
    raise RuntimeError("Solo está configurado para MySQL")
