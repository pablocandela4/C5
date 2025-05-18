"""
db_base.py

Define la interfaz base (DBManager) que deben implementar los gestores de
base de datos concretos (por ahora MySQL, pero extensible a SQLite u otros).
También carga las variables de entorno y expone la factoría `get_db_manager()`.
"""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

# ──────────────────────── 1) Variables de entorno ────────────────────────────
load_dotenv()

DB_TYPE = os.getenv("DB_TYPE", "mysql")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_NAME = os.getenv("DB_NAME", "clinica")
DB_USER = os.getenv("DB_USER", "")
DB_PASS = os.getenv("DB_PASS", "")

# ──────────────────────── 2) Interfaz genérica ───────────────────────────────
class DBManager(ABC):
    """Interfaz CRUD que usan el resto de capas de la aplicación."""

    # ── Animales ────────────────────────────────────────────────────────────
    @abstractmethod
    def insert_animal(self, datos: Dict[str, Any]) -> int:
        """Crea un animal y devuelve su ID."""
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

    # ── Dueños ──────────────────────────────────────────────────────────────
    @abstractmethod
    def insertar_dueno(self, datos: Dict[str, Any]) -> int:
        ...

    @abstractmethod
    def obtener_duenos(self) -> List[Dict[str, Any]]:
        ...

    @abstractmethod
    def obtener_dueno(self, dueno_id: int) -> Optional[Dict[str, Any]]:
        ...

    @abstractmethod
    def actualizar_dueno(self, dueno_id: int, datos: Dict[str, Any]) -> None:
        ...

    @abstractmethod
    def eliminar_dueno(self, dueno_id: int) -> None:
        ...

    # ── Veterinarios ────────────────────────────────────────────────────────
    @abstractmethod
    def insertar_veterinario(self, datos: Dict[str, Any]) -> int:
        ...

    @abstractmethod
    def obtener_veterinarios(self) -> List[Dict[str, Any]]:
        ...

    @abstractmethod
    def obtener_veterinario(self, colegiado_id: int) -> Optional[Dict[str, Any]]:
        ...

    @abstractmethod
    def actualizar_veterinario(self, colegiado_id: int, datos: Dict[str, Any]) -> None:
        ...

    @abstractmethod
    def eliminar_veterinario(self, colegiado_id: int) -> None:
        ...

    # ── Cuidados ────────────────────────────────────────────────────────────
    @abstractmethod
    def insert_cuidado(self, datos: Dict[str, Any]) -> int:
        ...

    @abstractmethod
    def get_cuidados(self, animal_id: Optional[int] = None) -> List[Dict[str, Any]]:
        ...

    @abstractmethod
    def update_cuidado(self, cuidado_id: int, datos: Dict[str, Any]) -> None:
        ...

    @abstractmethod
    def delete_cuidado(self, cuidado_id: int) -> None:
        ...

    # ── Alimentos ───────────────────────────────────────────────────────────
    @abstractmethod
    def insertar_alimento(self, datos: Dict[str, Any]) -> int:
        ...

    @abstractmethod
    def obtener_alimentos(self) -> List[Dict[str, Any]]:
        ...

    @abstractmethod
    def obtener_alimento(self, alimento_id: int) -> Optional[Dict[str, Any]]:
        ...

    @abstractmethod
    def actualizar_alimento(self, alimento_id: int, datos: Dict[str, Any]) -> None:
        ...

    @abstractmethod
    def eliminar_alimento(self, alimento_id: int) -> None:
        ...

    # ── Vacunas ──────────────────────────────────────────────────────────────
    @abstractmethod
    def insert_vacuna(self, datos: Dict[str, Any]) -> int:
        """Crea una vacuna y devuelve su ID."""
        ...

    @abstractmethod
    def listar_vacunas(self) -> List[Dict[str, Any]]:
        """Devuelve todas las vacunas como lista de dicts."""
        ...

    @abstractmethod
    def update_vacuna(self, vacuna_id: int, datos: Dict[str, Any]) -> None:
        """Actualiza los campos indicados en `datos` para la vacuna `vacuna_id`."""
        ...

    @abstractmethod
    def delete_vacuna(self, vacuna_id: int) -> None:
        """Elimina la vacuna con ID `vacuna_id`."""
        ...

    # ── Tratamientos ─────────────────────────────────────────────────────────
    @abstractmethod
    def insert_tratamiento(self, datos: Dict[str, Any]) -> int:
        """Crea un tratamiento y devuelve su ID."""
        ...

    @abstractmethod
    def listar_tratamientos(self) -> List[Dict[str, Any]]:
        """Devuelve todos los tratamientos como lista de dicts."""
        ...

    @abstractmethod
    def update_tratamiento(self, tratamiento_id: int, datos: Dict[str, Any]) -> None:
        """Actualiza los campos indicados en `datos` para el tratamiento `tratamiento_id`."""
        ...

    @abstractmethod
    def delete_tratamiento(self, tratamiento_id: int) -> None:
        """Elimina el tratamiento con ID `tratamiento_id`."""
        ...

    # ── Consultas ────────────────────────────────────────────────────────────
    @abstractmethod
    def insert_consulta(self, datos: Dict[str, Any]) -> int:
        """Crea una consulta y devuelve su ID."""
        ...

    @abstractmethod
    def listar_consultas(self) -> List[Dict[str, Any]]:
        """Devuelve todas las consultas como lista de dicts."""
        ...

    @abstractmethod
    def update_consulta(self, consulta_id: int, datos: Dict[str, Any]) -> None:
        """Actualiza los campos indicados en `datos` para la consulta `consulta_id`."""
        ...

    @abstractmethod
    def delete_consulta(self, consulta_id: int) -> None:
        """Elimina la consulta con ID `consulta_id`."""
        ...


# ──────────────────────── 3) Importa gestores concretos ──────────────────────
from .mysql_manager import MySQLManager   # noqa: E402

# ──────────────────────── 4) Factoría de gestores ────────────────────────────
def get_db_manager() -> DBManager:
    """
    Devuelve una instancia del gestor adecuado según la variable `DB_TYPE`.
    Actualmente solo se soporta MySQL.
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
