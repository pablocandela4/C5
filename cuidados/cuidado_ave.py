from cuidados.cuidado_base import CuidadoProgramado

class CuidadoAve(CuidadoProgramado):
    """
    Cuidado específico para aves.

    Hereda de CuidadoProgramado e implementa el método realizar_cuidado.
    """
    def realizar_cuidado(self):
        """
        Imprime una acción representativa del cuidado al ave.
        """
        print(f"Realizando '{self.tipo_cuidado}' al ave (ID: {self.animal_id}). ¡Pío pío contenta!")
