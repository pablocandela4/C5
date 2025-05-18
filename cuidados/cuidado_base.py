"""
cuidado_base.py

Clase abstracta CuidadoProgramado: representa un cuidado programado que se
almacena en la base de datos.  Sirve de clase padre para cuidados específicos
de perro, gato, ave y pez.

Atributos
---------
id : int | None
    Identificador primario en la tabla `cuidados`.  Lo asigna la BD.
animal_id : int
    Clave foránea al animal que recibe el cuidado.
fecha : datetime.date
    Día en el que debe realizarse el cuidado.
tipo_cuidado : str
    Descripción corta del cuidado (p. ej. "Vacuna", "Desparasitación").
estado : str
    Uno de {"pendiente", "realizado", "cancelado"}.
notas : str
    Información adicional libre.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime, date
from typing import Any, Dict, ClassVar, Final


class CuidadoProgramado(ABC):
    """Modelo base para un cuidado programado."""

    # valores permitidos para `estado`
    ESTADOS_VALIDOS: ClassVar[set[str]] = {"pendiente", "realizado", "cancelado"}

    def __init__(
        self,
        fecha: str | date,
        tipo_cuidado: str,
        *,
        animal_id: int,
        estado: str = "pendiente",
        notas: str = "",
        id: int | None = None,
    ) -> None:
        # ── Validaciones y normalizaciones ──────────────────────────────
        if isinstance(fecha, str):
            try:
                fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
            except ValueError as e:
                raise ValueError(
                    "La fecha debe estar en formato YYYY-MM-DD."
                ) from e

        if estado not in self.ESTADOS_VALIDOS:
            raise ValueError(
                f"Estado '{estado}' no válido; usa {self.ESTADOS_VALIDOS}.")

        # ── Asignación de atributos ─────────────────────────────────────
        self.id: int | None = id
        self.animal_id: int = animal_id
        self.fecha: date = fecha
        self.tipo_cuidado: str = tipo_cuidado
        self.estado: str = estado
        self.notas: str = notas

    # ─────────────────────────── Métodos de instancia ──────────────────────────
    def actualizar_estado(self, nuevo_estado: str) -> None:
        """Cambia el estado del cuidado si `nuevo_estado` es válido."""
        if nuevo_estado in self.ESTADOS_VALIDOS:
            self.estado = nuevo_estado
        else:
            raise ValueError(
                f"Estado '{nuevo_estado}' no válido; usa {self.ESTADOS_VALIDOS}."
            )

    def to_dict(self, include_id: bool = False) -> Dict[str, Any]:
        """
        Exporta a diccionario, útil para insertar/actualizar en MySQL.

        Parameters
        ----------
        include_id : bool
            Si `True` incluye el campo `id` aunque sea None.
        """
        data: Dict[str, Any] = {
            "animal_id": self.animal_id,
            "fecha": self.fecha.strftime("%Y-%m-%d"),
            "tipo": self.tipo_cuidado,
            "estado": self.estado,
            "notas": self.notas,
        }
        if include_id:
            data["id"] = self.id
        return data

    # ───────────────────────── Métodos de clase / fábrica ───────────────────────
    @classmethod
    def from_row(cls, row: Dict[str, Any]) -> "CuidadoProgramado":
        """
        Crea una instancia a partir de una fila dict proveniente de MySQL
        (`cursor(dictionary=True)`).

        *Para clases hijas*, sobreescribir cuando haya lógica adicional.
        """
        return cls(
            id=row.get("id"),
            animal_id=row["animal_id"],
            fecha=row["fecha"] if isinstance(row["fecha"], str) else row["fecha"].strftime("%Y-%m-%d"),
            tipo_cuidado=row["tipo"],
            estado=row["estado"],
            notas=row.get("notas", ""),
        )

    # ─────────────────────────── Representación ────────────────────────────────
    def __str__(self) -> str:          # para `print(cuidado)`
        fecha_txt = self.fecha.strftime("%Y-%m-%d")
        return (
            f"{self.tipo_cuidado} → animal {self.animal_id} "
            f"({fecha_txt}) · {self.estado}"
        )

    def __repr__(self) -> str:         # para debug / consola interactiva
        return (
            f"<{self.__class__.__name__} id={self.id} "
            f"animal_id={self.animal_id} tipo='{self.tipo_cuidado}' "
            f"fecha={self.fecha} estado='{self.estado}'>"
        )

    # ──────────────────────────── API pública ──────────────────────────────────
    @abstractmethod
    def realizar_cuidado(self) -> None:
        """
        Acción concreta del cuidado; la implementan las subclases.
        Debe llamar a `self.actualizar_estado("realizado")` cuando termine.
        """
        pass
