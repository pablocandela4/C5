"""
cuidado_ave.py

Cuidado específico para aves.
"""

from .cuidado_base import CuidadoProgramado


class CuidadoAve(CuidadoProgramado):
    """Aplica un cuidado a un ave."""

    def realizar_cuidado(self) -> None:
        self.actualizar_estado("realizado")
        print(f"🐦 Cuidado '{self.tipo_cuidado}' aplicado al ave (ID {self.animal_id}). ¡Pío pío contenta!")
