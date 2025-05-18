"""
cuidado_gato.py

Cuidado específico para gatos.
"""

from .cuidado_base import CuidadoProgramado


class CuidadoGato(CuidadoProgramado):
    """Aplica un cuidado a un gato."""

    def realizar_cuidado(self) -> None:
        self.actualizar_estado("realizado")
        print(f"😺 Cuidado '{self.tipo_cuidado}' aplicado al gato (ID {self.animal_id}).")
