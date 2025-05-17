"""
Clase base que define la interfaz mínima que deberán seguir
los gestores concretos (SQLite y MySQL).
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class DBManager(ABC):
    """Interfaz CRUD genérica."""

    # ---------- Animales ----------
    @abstractmethod
    def insert_animal(self, datos: Dict[str, Any]) -> int: ...
    @abstractmethod
    def get_animales(self) -> List[Dict[str, Any]]: ...
    @abstractmethod
    def update_animal(self, animal_id: int, datos: Dict[str, Any]) -> None: ...
    @abstractmethod
    def delete_animal(self, animal_id: int) -> None: ...

    # Aquí puedes añadir vacunas, cuidados, alimentos, etc.
