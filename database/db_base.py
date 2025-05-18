"""
db_base.py

Define la interfaz base (DBManager) que deben implementar los gestores de
base de datos concretos (por ahora MySQL, pero extensible a SQLite u otros).
También carga las variables de entorno y expone la factoría `get_db_manager()`.
"""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional

from dotenv import load_dotenv

# ──────────────────────── 1) Variables de entorno ────────────────────────────
load_dotenv()

DB_TYPE: str  = os.getenv("DB_TYPE", "mysql")      # «mysql» por defecto
DB_HOST: str  = os.getenv("DB_HOST", "localhost")
DB_PORT: int  = int(os.getenv("DB_PORT", 3306))
DB_NAME: str  = os.getenv("DB_NAME", "clinica")
DB_USER: str  = os.getenv("DB_USER", "")
DB_PASS: str  = os.getenv("DB_PASS", "")

# ──────────────────────── 2) Interfaz genérica ───────────────────────────────
class DBManager(ABC):
    """Interfaz CRUD que usan el resto de capas de la aplicación."""

    # ── Animales ────────────────────────────────────────────────────────────
    @abstractmethod
    def insert_animal(self, datos: Dict[str, Any]) -> int:
        """Crea un animal y devuelve su ID (chip)."""                                # noqa: D401
        ...

    @abstractmethod
    def get_animales(self) -> List[Dict[str, Any]]:
        """Devuelve todos los animales como lista de dicts."""
        ...

    @abstractmethod
    def update_animal(self, animal_id: int, datos: Dict[str, Any]) -> None:
        """Actualiza los campos indicados en `datos` para el animal `animal_id`."""
        ...

    @abstractmethod
    def delete_animal(self, animal_id: int) -> None:
        """Elimina el animal con ID `animal_id`."""
        ...

    # ── Cuidados ────────────────────────────────────────────────────────────
    @abstractmethod
    def insert_cuidado(self, datos: Dict[str, Any]) -> int:
        """
        Inserta un cuidado programado.
        `datos` debe contener: animal_id, fecha, tipo, estado (opcional), notas.
        Devuelve el ID autogenerado del cuidado.
        """
        ...

    @abstractmethod
    def get_cuidados(
        self,
        animal_id: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Devuelve los cuidados.  
        Si `animal_id` es `None`, devuelve todos; en caso contrario, solo
        los asociados al animal indicado.
        """
        ...

    @abstractmethod
    def update_cuidado(self, cuidado_id: int, datos: Dict[str, Any]) -> None:
        """Actualiza los campos indicados en `datos` para el cuidado `cuidado_id`."""
        ...

    @abstractmethod
    def delete_cuidado(self, cuidado_id: int) -> None:
        """Elimina el cuidado con ID `cuidado_id`."""
        ...

    # ---------- Alimentos ----------
    @abstractmethod
    def insertar_alimento(self, datos: Dict[str, Any]) -> int:
        """Inserta un nuevo alimento en la base de datos."""
        ...

    @abstractmethod
    def obtener_alimentos(self) -> List[Dict[str, Any]]:
        """Obtiene todos los alimentos de la base de datos."""
        ...

    @abstractmethod
    def obtener_alimento(self, alimento_id: int) -> Optional[Dict[str, Any]]:
        """Obtiene un alimento por su ID."""
        ...

    @abstractmethod
    def actualizar_alimento(self, alimento_id: int, datos: Dict[str, Any]) -> None:
        """Actualiza la información de un alimento existente."""
        ...

    @abstractmethod
    def eliminar_alimento(self, alimento_id: int) -> None:
        """Elimina un alimento de la base de datos."""
        ...


    @abstractmethod
    def delete_cuidado(self, cuidado_id: int) -> None:
        """Elimina el cuidado con ID `cuidado_id`."""
        ...

# ──────────────────────── 3) Importa gestores concretos ──────────────────────
from .mysql_manager import MySQLManager   # noqa: E402  (import después de ABC)

# ──────────────────────── 4) Factoría de gestores ────────────────────────────
def get_db_manager() -> DBManager:
    """
    Devuelve una instancia del gestor adecuado según la variable `DB_TYPE`.

    Por ahora solo está implementado MySQL.  Si quieres soporte para SQLite
    u otros motores, crea un fichero `sqlite_manager.py` que herede de
    `DBManager` e inclúyelo aquí.
    """
    if DB_TYPE.lower() == "mysql":
        return MySQLManager(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
        )

    raise RuntimeError(
        f"DB_TYPE='{DB_TYPE}' no está soportado. "
        "Implementa un gestor concreto o cambia la variable de entorno."
    )
