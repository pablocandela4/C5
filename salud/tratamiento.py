class Tratamiento:
    """
    Representa un tratamiento médico que se aplica a una animal.

    Atributos:
        nombre (str): Nombre del tratamiento
        fecha_inicio (str): Fecha de inicio del tratamiento.
        fecha_fin (str): Fecha de finalización del tratamiento.
        coste (float): Coste del tratamiento.
    """
    def __init__(self, nombre, fecha_inicio, fecha_fin, coste):
        """
        Inicializa una nueva instancia de Tratamiento.

        Args:
            nombre (str): Nombre del tratamiento.
            fecha_inicio (str): Fecha de inicio del tratamiento (formato string).
            fecha_fin (str): Fecha de finalización del tratamiento (formato string).
            coste (float): Coste económico del tratamiento.
        """
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.coste = coste

    def __str__(self):
        """
        Devuelve uan representación legible del tratamiento.

        Returns:
            str: Información formateada del tratamiento.
        """
        return f'{self.nombre}: FI. {self.fecha_inicio}, FF. {self.fecha_fin}, coste: {self.coste}'


class RegistroTratamientos:
    """
    Representa una lista de tratamientos aplicados a un animal.

    Atributos:
        tratamientos (list): Lista de tratamientos registrados.
    """
    def __init__(self):
        self.tratamientos = []

    def agregar_tratamiento(self, tratamiento):
        """
        Agrega un tratamiento a la lista.
        Args:
            tratamiento (Tratamiento): Instancia de la clase Tratamiento que se debe registrar
        """
        self.tratamientos.append(tratamiento)

    def __str__(self):
        """
        Devuelve una representación legible del registro de tratamientos.

        Returns:
             str: Lista de tratamientos o mensaje si está vacía.
        """
        if not self.tratamientos:
            return 'Sin tratamientos registrados.'
        return '\n'.join(f' - {t}' for t in self.tratamientos)
