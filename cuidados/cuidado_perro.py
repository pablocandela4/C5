"""
cuidado_perro.py

Cuidado específico para perros.
"""

from .cuidado_base import CuidadoProgramado


class CuidadoPerro(CuidadoProgramado):
    """Aplica un cuidado a un perro."""

    def realizar_cuidado(self) -> None:
        """Marca el cuidado como realizado y muestra un mensaje."""
        self.actualizar_estado("realizado")
        print(f"🐶 Cuidado '{self.tipo_cuidado}' aplicado al perro (ID {self.animal_id}).")
