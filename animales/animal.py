from vacunacion import CartillaVacunacion
from alimentacion import ListaAlimentos, Alimento
from cuidado_base import CuidadoProgramado


class Animal:
    """
    Clase base que representa un animal genérico. Los animales pueden tener un chip, un nombre, una especie,
    una edad y una cartilla de vacunación (opcionalmente).
    """

    def __init__(self, chip, nombre, especie, edad, requiere_cartilla=True, requiere_alimentos=True, requiere_cuidados=True):
        """
        Inicializa un nuevo animal.

        :param chip: El identificador del chip del animal (puede ser None si no tiene chip).
        :param nombre: El nombre del animal.
        :param especie: La especie del animal (por ejemplo, "Perro", "Gato").
        :param edad: La edad del animal en años.
        :param requiere_cartilla: Booleano que indica si el animal tiene una cartilla de vacunación (por defecto True).
        :param requiere_alimentos: Booleano que indica si el animal requiere una lista de alimentos (por defecto True).
        :param requiere_cuidados: Booleano que indica si el animal requiere cuidados programados (por defecto True).
        """
        self.requiere_alimentos = requiere_alimentos
        self.chip = chip
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.cartilla = CartillaVacunacion() if requiere_cartilla else None
        self.lista_alimentos = ListaAlimentos() if requiere_alimentos else None
        self.dueno = None
        self.cuidados_programados = [] if requiere_cuidados else []

    def __str__(self):
        """
        Representa al animal en formato legible como cadena de texto.

        :return: Cadena que describe el animal, su especie, su edad, chip, dueño (si tiene) y cartilla de vacunación (si la tiene),
                 junto con su lista de alimentos y cuidados programados.
        """
        chip_info = f", Chip: {self.chip}" if self.chip else ""
        dueno_info = f", Dueño: {self.dueno.nombre}" if self.dueno else ""
        cartilla_info = f"\nCartilla de vacunación:\n{self.cartilla}" if self.cartilla else ""
        alimentos_info = f"\nAlimentos:\n {self.lista_alimentos}" if self.lista_alimentos else ""
        cuidados_info = f"\nCuidados programados:\n{self.mostrar_cuidados()}" if self.cuidados_programados else ""
        base = f"{self.__class__.__name__}: {self.nombre} ({self.especie}, {self.edad} años{chip_info}{dueno_info})"
        return f"{base}{cartilla_info}{alimentos_info}{cuidados_info}"

    def __repr__(self):
        """
        Representación detallada del animal, útil para depuración.

        :return: Cadena con la representación interna del animal, incluyendo su nombre, especie, edad, chip, y cartilla de vacunación.
        """
        if self.cartilla:
            vacunas_repr = ", ".join(repr(v) for v in self.cartilla.vacunas) or "sin vacunas"
        else:
            vacunas_repr = "no aplica"
        dueno_info = f", dueno_nif={self.dueno.nif!r}" if self.dueno else ""
        return (
            f"{self.__class__.__name__}(nombre={self.nombre!r}, especie={self.especie!r}, "
            f"edad={self.edad!r}, chip={self.chip!r}, vacunas=[{vacunas_repr}]{dueno_info})"
        )

    def __eq__(self, other):
        """
        Compara dos animales para ver si son iguales según su chip.

        :param other: Otro objeto de tipo Animal.
        :return: True si los animales son iguales (mismo chip), False en caso contrario.
        """
        if not isinstance(other, Animal):
            return False
        return self.chip == other.chip

    def vacunar(self, vacuna):
        """
        Vacuna al animal, si tiene una cartilla de vacunación.

        :param vacuna: El nombre de la vacuna a aplicar (debe ser una cadena de texto).
        :raises AttributeError: Si el animal no tiene cartilla de vacunación.
        """
        try:
            if self.cartilla:
                nueva_vacuna = Vacuna(vacuna, "2025-04-10")  # Se crea un objeto Vacuna con el nombre y una fecha de ejemplo
                self.cartilla.agregar_vacuna(nueva_vacuna)
                print(f"{self.nombre} ha sido vacunado con {vacuna}.")
            else:
                raise AttributeError(f"{self.__class__.__name__} no puede ser vacunado porque no tiene cartilla.")
        except AttributeError as e:
            print(f"Error: {e}")

    def alimentar(self, alimento: Alimento):
        """
        Alimenta al animal, agregando un alimento a su lista de alimentos.

        :param alimento: Un objeto de tipo Alimento que será agregado a la lista del animal.
        """
        if self.lista_alimentos:
            self.lista_alimentos.agregar_alimento(alimento)
            print(f"{self.nombre} ha sido alimentado con {alimento.alimento}.")
        else:
            print(f"{self.nombre} no tiene lista de alimentos.")

    def asignar_alimentos(self, catalogo):
        """
        Asigna alimentos del catálogo según el tipo de animal.

        :param catalogo: Lista de alimentos disponibles de tipo Alimento.
        """
        if self.lista_alimentos:
            alimentos_disponibles = [alimento for alimento in catalogo if alimento.tipo_animal == self.especie.lower()]
            for alimento in alimentos_disponibles:
                self.lista_alimentos.agregar_alimento(alimento)
            print(f"Alimentos asignados a {self.nombre}: {', '.join([a.alimento for a in alimentos_disponibles])}")
        else:
            print(f"{self.nombre} no tiene lista de alimentos asignada.")

    def asignar_cuidado(self, cuidado: CuidadoProgramado):
        """
        Asigna un cuidado programado al animal.

        :param cuidado: Un objeto de tipo CuidadoProgramado que se asignará al animal.
        """
        if self.requiere_cuidados:
            self.cuidados_programados.append(cuidado)
            print(f"{self.nombre} tiene un nuevo cuidado programado: {cuidado.tipo_cuidado} para el {cuidado.fecha.date()}.")
        else:
            print(f"{self.nombre} no requiere cuidados programados.")

    def mostrar_cuidados(self):
        """
        Muestra los cuidados programados para el animal de forma legible.

        :return: Una cadena con la lista de cuidados programados o un mensaje indicando que no hay cuidados programados.
        """
        if self.cuidados_programados:
            return "\n".join(str(cuidado) for cuidado in self.cuidados_programados)
        else:
            return "  - No hay cuidados programados."


class Perro(Animal):
    """
    Clase que representa un perro, heredada de la clase Animal. Un perro tiene una raza además de las características comunes de un animal.
    """

    def __init__(self, chip, nombre, edad, raza):
        """
        Inicializa un nuevo perro.

        :param chip: El identificador del chip del perro.
        :param nombre: El nombre del perro.
        :param edad: La edad del perro en años.
        :param raza: La raza del perro.
        """
        super().__init__(chip, nombre, "Perro", edad)
        self.raza = raza

    def __str__(self):
        """
        Representación legible del perro en formato cadena de texto.

        :return: Cadena que describe al perro, incluyendo su raza y cartilla de vacunación (si la tiene).
        """
        cartilla_info = f"\nCartilla de vacunación:\n{self.cartilla}" if self.cartilla else ""
        return (
            f"{self.__class__.__name__}: {self.nombre} ({self.especie}, {self.edad} años, "
            f"Raza: {self.raza}, Chip: {self.chip}){cartilla_info}"
        )

    def __repr__(self):
        """
        Representación detallada del perro para depuración.

        :return: Cadena que representa al perro, con información sobre su raza y cartilla de vacunación.
        """
        base = super().__repr__()[:-1]
        return f"{base}, raza={self.raza!r})"


class Gato(Animal):
    """
    Clase que representa un gato, heredada de la clase Animal. Un gato tiene una raza además de las características comunes de un animal.
    """

    def __init__(self, chip, nombre, edad, raza):
        """
        Inicializa un nuevo gato.

        :param chip: El identificador del chip del gato.
        :param nombre: El nombre del gato.
        :param edad: La edad del gato en años.
        :param raza: La raza del gato.
        """
        super().__init__(chip, nombre, "Gato", edad)
        self.raza = raza

    def __str__(self):
        """
        Representación legible del gato en formato cadena de texto.

        :return: Cadena que describe al gato, incluyendo su raza y cartilla de vacunación (si la tiene).
        """
        cartilla_info = f"\nCartilla de vacunación:\n{self.cartilla}" if self.cartilla else ""
        return (
            f"{self.__class__.__name__}: {self.nombre} ({self.especie}, {self.edad} años, "
            f"Raza: {self.raza}, Chip: {self.chip}){cartilla_info}"
        )

    def __repr__(self):
        """
        Representación detallada del gato para depuración.

        :return: Cadena que representa al gato, con información sobre su raza y cartilla de vacunación.
        """
        base = super().__repr__()[:-1]
        return f"{base}, raza={self.raza!r})"


class Ave(Animal):
    """
    Clase que representa un ave, heredada de la clase Animal. Las aves no requieren cartilla de vacunación.
    """

    def __init__(self, nombre, edad):
        """
        Inicializa un nuevo ave. No tiene cartilla de vacunación.

        :param nombre: El nombre del ave.
        :param edad: La edad del ave en años.
        """
        super().__init__(None, nombre, "Ave", edad, requiere_cartilla=False)

    def __str__(self):
        """
        Representación legible del ave en formato cadena de texto.

        :return: Cadena que describe al ave, incluyendo su especie y edad.
        """
        return f"{self.__class__.__name__}: {self.nombre} ({self.especie}, {self.edad} años)"

    def __repr__(self):
        """
        Representación detallada del ave para depuración.

        :return: Cadena que representa al ave, sin cartilla de vacunación.
        """
        base = super().__repr__()[:-1]
        return f"{base})"


class Pez(Animal):
    """
    Clase que representa un pez, heredada de la clase Animal. Los peces no requieren cartilla de vacunación.
    """

    def __init__(self, nombre, edad):
        """
        Inicializa un nuevo pez. No tiene cartilla de vacunación.

        :param nombre: El nombre del pez.
        :param edad: La edad del pez en años.
        """
        super().__init__(None, nombre, "Pez", edad, requiere_cartilla=False)

    def __str__(self):
        """
        Representación legible del pez en formato cadena de texto.

        :return: Cadena que describe al pez, incluyendo su especie y edad.
        """
        return f"{self.__class__.__name__}: {self.nombre} ({self.especie}, {self.edad} años)"

    def __repr__(self):
        """
        Representación detallada del pez para depuración.

        :return: Cadena que representa al pez, sin cartilla de vacunación
        """
        base = super().__repr__()[:-1]
        return f"{base})"





