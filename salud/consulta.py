import requests


class Consulta:
    """
    Representa una consulta médica realizada a un animal por un veterinario.

    Atributos:
        animal (Animal): El animal que recibió la consulta.
        veterinario (Veterinario): El veterinario que atendió la consulta.
        fecha (str): Fecha en que se realizó la consulta.
        diagnostico (str): Diagnóstico emitido por el veterinario.
    """
    def __init__(self, animal, veterinario, fecha, diagnostico):
        """
        Inicializa una nueva instancia de Consulta.

        Args:
            animal (Animal): Instancia del animal atendido.
            veterinario (Veterinario): Veterinario que realizó la consulta.
            fecha (str): Fecha de la consulta (formato string).
            diagnostico (str): Diagnóstico médico del animal.
        """
        self.animal = animal
        self.veterinario = veterinario
        self.fecha = fecha
        self.diagnostico = diagnostico
        requests.post("http://127.0.0.1:5000/tratamiento", json={"animal": self.animal, "veterinario": self.veterinario, "fecha": self.fecha, "diagnostico": self.diagnostico})

    def __str__(self):
        """
        Devuelve una representación legible de la consulta.

        Returns:
            str: Descripción con nombres, fecha y diagnóstico.
        """
        return (
            f"Consulta de {self.animal.nombre} con {self.veterinario.nombre} "
            f"el {self.fecha}: {self.diagnostico}"
        )

    def __repr__(self):
        """
        Devuelve una representación detallada de la consulta, útil para depuración.

        Returns:
            str: Representación técnica de la consulta.
        """
        return (
            f"Consulta(animal={self.animal.nombre!r}, "
            f"veterinario={self.veterinario.colegiado_id!r}, "
            f"fecha={self.fecha!r}, "
            f"diagnostico={self.diagnostico!r})"
        )