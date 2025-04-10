"""
cuidado_gato.py

Define la clase CuidadoGato, que representa un cuidado específico para gatos.

Hereda de:
    CuidadoProgramado
"""

from .cuidado_base import CuidadoProgramado

class CuidadoGato(CuidadoProgramado):
    def realizar_cuidado(self):
        """
        Realiza el cuidado específico para gatos.

        Imprime un mensaje indicando que el cuidado ha sido realizado.
        """
        print(f"Aplicando '{self.tipo_cuidado}' al gato (ID: {self.animal_id}). ¡El minino está feliz!")
