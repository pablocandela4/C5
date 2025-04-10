from datetime import datetime
from typing import List

class Alimento:
    """
    Representa un alimento para un animal.

    Atributos:
        tipo_animal (str): Tipo de animal al que está destinado el alimento.
        alimento (str): Nombre del alimento.
        cantidad (int): Cantidad de alimento en gramos.
        fecha_caducidad (str): Fecha de caducidad del alimento (formato string).
        coste (float): Precio del alimento en euros.
    """
    def __init__(self, tipo_animal, alimento, cantidad, fecha_caducidad, coste):
        """
        Inicializa una nueva instancia de Alimento.

        Args:
            tipo_animal (str): Tipo de animal (ej. perro, gato).
            alimento (str): Nombre del alimento.
            cantidad (int): Cantidad en gramos.
            fecha_caducidad (str): Fecha de caducidad (formato string).
            coste (float): Precio en euros.
        """
        self.tipo_animal = tipo_animal
        self.alimento = alimento
        self.cantidad = cantidad
        self.fecha_caducidad = fecha_caducidad
        self.coste = coste

    def __str__(self):
        """
        Devuelve una representación legible del alimento.

        Returns:
            str: Información sobre el alimento.
        """
        return f"{self.alimento} ({self.tipo_animal}) - {self.cantidad}g, caduca el {self.fecha_caducidad}, precio: {self.coste}€"


class CatalogoAlimentos:
    """
    Representa un catálogo de alimentos para animales.

    Atributos:
        alimentos (list): Lista de alimentos disponibles.
    """
    def __init__(self):
        """
        Inicializa un catálogo vacío.
        """
        self.alimentos = []

    def agregar_alimento(self, alimento):
        """
        Agrega un alimento al catálogo.

        Args:
            alimento (Alimento): Instancia de la clase Alimento a agregar.
        """
        self.alimentos.append(alimento)

    def __str__(self):
        """
        Devuelve una representación legible del catálogo de alimentos.

        Returns:
            str: Lista de alimentos o mensaje si está vacío.
        """
        if not self.alimentos:
            return "  - Sin alimentos registrados"
        return "\n".join(f"  - {a}" for a in self.alimentos)