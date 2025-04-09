from vacunacion import CartillaVacunacion


# from logica.vacunacion import CartillaVacunacion

class Animal:
    """
    Clase base que representa un animal genérico. Los animales pueden tener un chip, un nombre, una especie,
    una edad y una cartilla de vacunación (opcionalmente).
    """

    def __init__(self, chip, nombre, especie, edad, requiere_cartilla=True):
        """
        Inicializa un nuevo animal.

        :param chip: El identificador del chip del animal (puede ser None si no tiene chip).
        :param nombre: El nombre del animal.
        :param especie: La especie del animal (por ejemplo, "Perro", "Gato").
        :param edad: La edad del animal en años.
        :param requiere_cartilla: Booleano que indica si el animal tiene una cartilla de vacunación.
        """
        self.chip = chip
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.cartilla = CartillaVacunacion() if requiere_cartilla else None
        self.dueno = None

    def __str__(self):
        """
        Representa al animal en formato legible como cadena de texto.

        :return: Cadena que describe el animal, su especie, su edad, chip, dueño (si tiene) y cartilla de vacunación (si la tiene).
        """
        chip_info = f", Chip: {self.chip}" if self.chip else ""
        dueno_info = f", Dueño: {self.dueno.nombre}" if self.dueno else ""
        cartilla_info = f"\nCartilla de vacunación:\n{self.cartilla}" if self.cartilla else ""
        base = f"{self.__class__.__name__}: {self.nombre} ({self.especie}, {self.edad} años{chip_info}{dueno_info})"
        return f"{base}{cartilla_info}"

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

        :param vacuna: El nombre de la vacuna a aplicar.
        :raises AttributeError: Si el animal no tiene cartilla de vacunación.
        """
        try:
            if self.cartilla:
                self.cartilla.agregar_vacuna(vacuna)
                print(f"{self.nombre} ha sido vacunado con {vacuna}.")
            else:
                raise AttributeError(f"{self.__class__.__name__} no puede ser vacunado porque no tiene cartilla.")
        except AttributeError as e:
            print(f"Error: {e}")


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

        :return: Cadena que representa al pez, sin cartilla de vacunación.
        """
        base = super().__repr__()[:-1]
        return f"{base})"


if __name__ == "__main__":
    p = Perro("X54612", "Luna", 3, "Beagle")
    g = Gato("H3456", "Misi", 2, "Siames")
    a = Ave("Piolín", 1)
    pez = Pez("Nemo", 2)

    print("=== PERRO ===")
    print(str(p))
    print(repr(p))
    p.vacunar("Vacuna Antirrábica")
    print()

    print("=== GATO ===")
    print(str(g))
    print(repr(g))
    g.vacunar("Vacuna Antirrábica")
    print()

    print("=== AVE ===")
    print(str(a))
    print(repr(a))
    a.vacunar("Vacuna Antirrábica")  # No tiene cartilla, se lanzará una excepción
    print()

    print("=== PEZ ===")
    print(str(pez))
    print(repr(pez))
    pez.vacunar("Vacuna Antirrábica")  # No tiene cartilla, se lanzará una excepción
    print()
