"""
cuidado_ave.py

Define la clase CuidadoAve, que representa un cuidado específico para aves.

Hereda de:
    CuidadoProgramado
"""

from .cuidado_base import CuidadoProgramado

class CuidadoAve(CuidadoProgramado):
    def realizar_cuidado(self):
        """
        Realiza el cuidado específico para aves.

        Imprime un mensaje indicando que el cuidado ha sido realizado.
        """
        print(f"Realizando '{self.tipo_cuidado}' al ave (ID: {self.animal_id}). ¡Pío pío contenta!")
