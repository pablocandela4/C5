"""
cuidado_perro.py

Define la clase CuidadoPerro, que representa un cuidado específico para perros.

Hereda de:
    CuidadoProgramado
"""

from .cuidado_base import CuidadoProgramado

class CuidadoPerro(CuidadoProgramado):
    def realizar_cuidado(self):
        """
        Realiza el cuidado específico para perros.

        Imprime un mensaje indicando que el cuidado ha sido realizado.
        """
        print(f"Realizando '{self.tipo_cuidado}' al perro (ID: {self.animal_id})")
