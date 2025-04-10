class Vacuna:
    """
    Representa una vacuna administrada a un animal.

    Atributos:
        nombre (str): Nombre de la vacuna.
        fecha (str): Fecha en que fue administrada.
    """
    def __init__(self, nombre, fecha):
        """
        Inicializa una nueva instancia de Vacuna.

        Args:
            nombre (str): Nombre de la vacuna.
            fecha (str): Fecha de administración (formato string).
        """
        self.nombre = nombre
        self.fecha = fecha

    def __str__(self):
        """
        Devuelve una representación legible de la vacuna.

        Returns:
            str: Nombre de la vacuna y fecha de aplicación.
        """
        return f"{self.nombre} ({self.fecha})"


class CartillaVacunacion:
    """
    Representa una cartilla de vacunación para un animal.

    Atributos:
        vacunas (list): Lista de vacunas administradas.
    """
    def __init__(self):
        """
        Inicializa una nueva cartilla sin vacunas registradas.
        """
        self.vacunas = []

    def agregar_vacuna(self, vacuna):
        """
        Agrega una vacuna a la cartilla de vacunación.

        Args:
            vacuna (Vacuna): Instancia de la clase Vacuna a registrar.
        """
        self.vacunas.append(vacuna)

    def __str__(self):
        """
        Devuelve una representación legible de la cartilla de vacunación.

        Returns:
            str: Lista de vacunas o mensaje si está vacía.
        """
        if not self.vacunas:
            return "  - Sin vacunas registradas"
        return "\n".join(f"  - {v}" for v in self.vacunas)