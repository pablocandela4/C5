"""
cuidado_base.py

Define la clase abstracta CuidadoProgramado, que representa un cuidado programado para un animal.

Atributos:
    fecha (datetime): Fecha del cuidado.
    tipo_cuidado (str): Tipo de cuidado.
    estado (str): Estado del cuidado ('pendiente', 'realizado', 'cancelado').
    notas (str): Información adicional del cuidado.
    animal_id (int): Identificador del animal asociado al cuidado.
"""

from abc import ABC, abstractmethod
from datetime import datetime

class CuidadoProgramado(ABC):
    def __init__(self, fecha: str, tipo_cuidado: str, estado: str = "pendiente", notas: str = "", animal_id: int = None):
        """
        Inicializa una nueva instancia de CuidadoProgramado.

        Args:
            fecha (str): Fecha del cuidado en formato "YYYY-MM-DD".
            tipo_cuidado (str): Tipo de cuidado programado.
            estado (str): Estado del cuidado. Por defecto es 'pendiente'.
            notas (str): Notas adicionales sobre el cuidado.
            animal_id (int): ID del animal al que se le asigna el cuidado.
        """
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d")
        self.tipo_cuidado = tipo_cuidado
        self.estado = estado
        self.notas = notas
        self.animal_id = animal_id

    def actualizar_estado(self, nuevo_estado: str):
        """
        Actualiza el estado del cuidado.

        Args:
            nuevo_estado (str): Nuevo estado ('pendiente', 'realizado', 'cancelado').

        Raises:
            ValueError: Si el estado no es válido.
        """
        if nuevo_estado in ["pendiente", "realizado", "cancelado"]:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado inválido. Usa 'pendiente', 'realizado' o 'cancelado'.")

    def __str__(self):
        """
        Devuelve una representación legible del cuidado.

        Returns:
            str: Descripción del cuidado con fecha, tipo y estado.
        """
        return f"{self.tipo_cuidado} para animal {self.animal_id} el {self.fecha.date()} - Estado: {self.estado}"

    @abstractmethod
    def realizar_cuidado(self):
        """
        Método abstracto que define la acción del cuidado.
        Debe ser implementado en las subclases.
        """
        pass
