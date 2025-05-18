"""
cuidado_pez.py

Cuidado específico para peces.
"""

from .cuidado_base import CuidadoProgramado


class CuidadoPez(CuidadoProgramado):
    """Aplica un cuidado a un pez."""

    def realizar_cuidado(self) -> None:
        self.actualizar_estado("realizado")
        print(f"🐟 Cuidado '{self.tipo_cuidado}' aplicado al pez (ID {self.animal_id}). ¡Agua limpia y peces felices!")
