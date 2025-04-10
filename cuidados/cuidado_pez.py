"""
cuidado_pez.py

Define la clase CuidadoPez, que representa un cuidado específico para peces.

Hereda de:
    CuidadoProgramado
"""

from .cuidado_base import CuidadoProgramado

class CuidadoPez(CuidadoProgramado):
    def realizar_cuidado(self):
        """
        Realiza el cuidado específico para peces.

        Imprime un mensaje indicando que el cuidado ha sido realizado.
        """
        print(f"Ejecutando '{self.tipo_cuidado}' al pez (ID: {self.animal_id}). ¡Agua limpia y peces felices!")
