from abc import ABC, abstractmethod

class Persona(ABC):
    """
    Clase abstracta base que representa una persona.

    Atributos:
        nombre (str): Nombre de la persona.
        nif (str): Número de identificación fiscal.
        direccion (str): Dirección física.
        telefono (str): Número de teléfono.
    """
    def __init__(self, nombre, nif, direccion, telefono):
        """
        Inicializa una nueva instancia de Persona.

        Args:
            nombre (str): Nombre de la persona.
            nif (str): Número de identificación fiscal.
            direccion (str): Dirección física.
            telefono (str): Número de teléfono.
        """
        self.nombre = nombre
        self.nif = nif
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        """
        Devuelve una representación legible de la persona.

        Returns:
            str: Cadena con el nombre, NIF y teléfono.
        """
        return f"{self.__class__.__name__}: {self.nombre}, NIF: {self.nif}, Tel: {self.telefono}"

    def __repr__(self):
        """
        Devuelve una representación detallada para depuración.

        Returns:
            str: Representación con todos los atributos.
        """
        return (f"{self.__class__.__name__}(nombre={self.nombre!r}, "
                f"nif={self.nif!r},direccion={self.direccion!r}, telefono={self.telefono!r})")

    def __eq__(self, other):
        """
        Compara dos objetos Persona por su NIF.

        Args:
            other (Persona): Otro objeto Persona a comparar.

        Returns:
            bool: True si tienen el mismo NIF, False en caso contrario.
        """
        if isinstance(other, Persona):
            return (self.nif == other.nif)
        return False


class Dueno(Persona):
    """
    Representa a un dueño de animales.

    Atributos heredados de Persona y:
        animales (list): Lista de animales asociados al dueño.
    """
    def __init__(self, nombre, nif, direccion, telefono):
        """
        Inicializa un nuevo dueño sin animales registrados.

        Args:
            nombre (str): Nombre del dueño.
            nif (str): Número de identificación fiscal.
            direccion (str): Dirección física.
            telefono (str): Número de teléfono.
        """
        super().__init__(nombre, nif, direccion, telefono)
        self.animales = []

    def agregar_animal(self, animal):
        """
        Agrega un animal a la lista del dueño.

        Args:
            animal (Animal): Instancia del animal a agregar.
        """
        self.animales.append(animal)

    def __str__(self):
        """
        Devuelve una representación legible del dueño y sus animales.

        Returns:
            str: Información del dueño y lista de sus animales.
        """
        encabezado = f"{self.__class__.__name__}: {self.nombre} (NIF: {self.nif})"
        if not self.animales:
            return f"{encabezado}\n  - Sin animales registrados"
        lista = "\n".join(f"  - {a.nombre} ({a.especie})" for a in self.animales)
        return f"{encabezado}\nAnimales:\n{lista}"

    def __repr__(self):
        """
        Devuelve una representación detallada del dueño.

        Returns:
            str: Información del dueño incluyendo número de animales.
        """
        base = super().__repr__()[:-1]  # Quitamos el cierre final del paréntesis
        return f"{base}, animales={len(self.animales)})"


class Veterinario(Persona):
    """
    Representa a un veterinario que atiende consultas.

    Atributos heredados de Persona y:
        colegiado_id (str): Identificador del colegio profesional.
        consultas (list): Lista de consultas atendidas.
    """
    def __init__(self, nombre, nif, direccion, telefono, colegiado_id):
        """
        Inicializa un nuevo veterinario sin consultas registradas.

        Args:
            nombre (str): Nombre del veterinario.
            nif (str): Número de identificación fiscal.
            direccion (str): Dirección física.
            telefono (str): Número de teléfono.
            colegiado_id (str): ID del colegio profesional.
        """
        super().__init__(nombre, nif, direccion, telefono)
        self.colegiado_id = colegiado_id
        self.consultas = []

    def __str__(self):
        """
        Devuelve una representación legible del veterinario y sus consultas.

        Returns:
            str: Información del veterinario y lista de sus consultas.
        """
        encabezado = f"{self.__class__.__name__}: {self.nombre} (ID: {self.colegiado_id})"
        if not self.consultas:
            return f"{encabezado}\n  - Sin consultas registradas"
        lista = "\n".join(f"  - {c.fecha}: {c.animal.nombre} → {c.diagnostico}" for c in self.consultas)
        return f"{encabezado}\nConsultas:\n{lista}"

    def __repr__(self):
        """
        Devuelve una representación detallada del veterinario.

        Returns:
            str: Información con ID de colegiado y número de consultas.
        """
        base = super().__repr__()[:-1]
        return f"{base}, colegiado_id={self.colegiado_id!r}, consultas={len(self.consultas)})"

    def registrar_consulta(self, consulta):
        """
        Registra una nueva consulta médica.

        Args:
            consulta (Consulta): Consulta realizada al animal.
        """
        self.consultas.append(consulta)    
