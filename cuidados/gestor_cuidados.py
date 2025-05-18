"""
gestor_cuidados.py

Funciones de alto nivel para crear, leer, actualizar y borrar cuidados
usando la capa `database.db` (cualquier gestor que implemente DBManager).


Uso básico
----------
from cuidados import gestor_cuidados as gc

# Crear
nuevo_id = gc.crear_cuidado(
    animal_id=3,
    fecha="2024-06-05",
    tipo_cuidado="Vacuna tetravalente",
    notas="Refuerzo anual"
)

# Listar
for c in gc.listar_cuidados(animal_id=3, as_objects=True):
    print(c)

# Marcar como realizado
gc.cambiar_estado_cuidado(nuevo_id, "realizado")
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Dict, Iterable, List, Optional

from database import db
from .cuidado_base import CuidadoProgramado
from .cuidado_perro import CuidadoPerro
from .cuidado_gato import CuidadoGato
from .cuidado_ave import CuidadoAve
from .cuidado_pez import CuidadoPez

# ---------------------------------------------------------------------------#
#  Helpers de conversión fila <-> objeto
# ---------------------------------------------------------------------------#

# Cache sencilla de animales → tipo, para instanciar la subclase correcta
# Se carga bajo demanda en _get_tipo_animal().
_ANIMALES_CACHE: Dict[int, str] = {}


def _get_tipo_animal(animal_id: int) -> Optional[str]:
    """Devuelve 'perro', 'gato', … para un animal o None si no se encuentra."""
    if animal_id in _ANIMALES_CACHE:
        return _ANIMALES_CACHE[animal_id]

    for a in db.get_animales():
        _ANIMALES_CACHE[a["chip"]] = a["tipo"].lower()

    return _ANIMALES_CACHE.get(animal_id)


_CLASE_POR_TIPO: Dict[str, type[CuidadoProgramado]] = {
    "perro": CuidadoPerro,
    "gato": CuidadoGato,
    "ave": CuidadoAve,
    "pez": CuidadoPez,
}


def _row_to_obj(row: Dict[str, Any]) -> CuidadoProgramado:
    """
    Convierte una fila dict de la tabla `cuidados` a la subclase adecuada.
    Si el tipo de animal no se reconoce, usa `CuidadoProgramado`.
    """
    tipo_animal = _get_tipo_animal(row["animal_id"])
    cls = _CLASE_POR_TIPO.get(tipo_animal, CuidadoProgramado)
    return cls.from_row(row)


# ---------------------------------------------------------------------------#
#  CRUD de cuidados
# ---------------------------------------------------------------------------#
def crear_cuidado(
    *,
    animal_id: int,
    fecha: str | date,
    tipo_cuidado: str,
    estado: str = "pendiente",
    notas: str = "",
) -> int:
    """
    Inserta un nuevo cuidado y devuelve su ID.

    Parameters
    ----------
    animal_id : int
        ID del animal que recibirá el cuidado.
    fecha : str | datetime.date
        Día programado (cadena 'YYYY-MM-DD' o date).
    tipo_cuidado : str
    estado : str, optional
    notas : str, optional
    """
    if isinstance(fecha, date):
        fecha = fecha.strftime("%Y-%m-%d")

    datos = {
        "animal_id": animal_id,
        "fecha": fecha,
        "tipo": tipo_cuidado,
        "estado": estado,
        "notas": notas,
    }
    return db.insert_cuidado(datos)


def listar_cuidados(
    animal_id: Optional[int] = None,
    *,
    as_objects: bool = False,
) -> List[Any]:
    """
    Devuelve los cuidados (todos o filtrados por animal).

    Parameters
    ----------
    animal_id : int | None
        Si se indica, solo los del animal.  Si None, lista global.
    as_objects : bool
        - `False` (por defecto): devuelve dicts tal cual vienen de la BD.
        - `True` : devuelve instancias de las subclases de cuidado.
    """
    filas = db.get_cuidados(animal_id)

    if not as_objects:
        return filas

    return [_row_to_obj(f) for f in filas]


def actualizar_cuidado(cuidado_id: int, cambios: Dict[str, Any]) -> None:
    """
    Modifica los campos indicados en `cambios` (clave/valor).
    Ejemplo: `{"notas": "Se reprograma", "fecha": "2024-06-12"}`
    """
    if not cambios:
        return
    db.update_cuidado(cuidado_id, cambios)


def cambiar_estado_cuidado(cuidado_id: int, nuevo_estado: str) -> None:
    """Atajo para solo cambiar el estado."""
    db.update_cuidado(cuidado_id, {"estado": nuevo_estado})


def borrar_cuidado(cuidado_id: int) -> None:
    """Elimina el cuidado indicado."""
    db.delete_cuidado(cuidado_id)


# ---------------------------------------------------------------------------#
#  Funciones de presentación (opcional)
# ---------------------------------------------------------------------------#
def mostrar_cuidados(
    animal_id: Optional[int] = None,
    *,
    ancho: int = 80,
) -> None:
    """
    Imprime una vista tabulada por consola (útil para depuración rápida).
    """
    cuidados = listar_cuidados(animal_id, as_objects=True)

    if not cuidados:
        print("No hay cuidados registrados.")
        return

    sep = "-" * ancho
    print(sep)
    for c in cuidados:
        print(f"{c.id:>3} | {c.fecha} | {c.tipo_cuidado[:20]:<20} | "
              f"Animal {c.animal_id:<3} | {c.estado:<10} | {c.notas}")
    print(sep)
