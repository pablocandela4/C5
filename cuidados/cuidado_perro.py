from cuidados.cuidado_base import CuidadoProgramado

class CuidadoPerro(CuidadoProgramado):
    """
    Cuidado específico para perros.

    Hereda de CuidadoProgramado e implementa el método realizar_cuidado.
    """
    def realizar_cuidado(self):
        """
        Imprime una acción representativa del cuidado al perro.
        """
        print(f"Realizando '{self.tipo_cuidado}' al perro (ID: {self.animal_id})")
