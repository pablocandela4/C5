from cuidados.cuidado_base import CuidadoProgramado

class CuidadoGato(CuidadoProgramado):
    """
    Cuidado específico para gatos.

    Hereda de CuidadoProgramado e implementa el método realizar_cuidado.
    """
    def realizar_cuidado(self):
        """
        Imprime una acción representativa del cuidado al gato.
        """
        print(f"Aplicando '{self.tipo_cuidado}' al gato (ID: {self.animal_id}). ¡El minino está feliz!")
