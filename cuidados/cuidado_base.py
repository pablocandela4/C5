from abc import ABC, abstractmethod
from datetime import datetime

class CuidadoProgramado(ABC):
    """
    Clase abstracta que representa un cuidado programado para una mascota.

    Atributos:
        fecha (datetime): Fecha del cuidado.
        tipo_cuidado (str): Descripción del tipo de cuidado.
        estado (str): Estado actual del cuidado ('pendiente', 'realizado', 'cancelado').
        notas (str): Información adicional sobre el cuidado.
        animal_id (int): Identificador del animal asociado.
    """
    def __init__(self, fecha: str, tipo_cuidado: str, estado: str = "pendiente", notas: str = "", animal_id: int = None):
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d")
        self.tipo_cuidado = tipo_cuidado
        self.estado = estado
        self.notas = notas
        self.animal_id = animal_id

    def actualizar_estado(self, nuevo_estado: str):
        """
        Actualiza el estado del cuidado.

        Args:
            nuevo_estado (str): 'pendiente', 'realizado' o 'cancelado'.

        Raises:
            ValueError: Si el estado no es válido.
        """
        if nuevo_estado in ["pendiente", "realizado", "cancelado"]:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado inválido. Usa 'pendiente', 'realizado' o 'cancelado'.")

    def __str__(self):
        return f"{self.tipo_cuidado} para animal {self.animal_id} el {self.fecha.date()} - Estado: {self.estado}"

    @abstractmethod
    def realizar_cuidado(self):
        """
        Método abstracto que define la acción del cuidado.
        Debe ser implementado en las subclases.
        """
        pass
