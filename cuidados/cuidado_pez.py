from cuidados.cuidado_base import CuidadoProgramado

class CuidadoPez(CuidadoProgramado):
    """
    Cuidado específico para peces.

    Hereda de CuidadoProgramado e implementa el método realizar_cuidado.
    """
    def realizar_cuidado(self):
        """
        Imprime una acción representativa del cuidado al pez.
        """
        print(f"Ejecutando '{self.tipo_cuidado}' al pez (ID: {self.animal_id}). ¡Agua limpia y peces felices!")
