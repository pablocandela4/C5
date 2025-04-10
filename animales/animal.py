"""
Este módulo define una jerarquía de clases para representar animales que pueden
ser vacunados, alimentados, recibir cuidados programados y tratamientos médicos.
Incluye especializaciones como Perro, Gato, Ave y Pez.

También se integra con módulos externos para gestionar alimentación, vacunación y tratamientos,
así como un pequeño bloque de ejemplo para uso práctico al ejecutar el archivo como script principal.
"""
from alimentacion import CatalogoAlimentos, Alimento
from vacunacion import CartillaVacunacion, Vacuna
from cuidado_base import CuidadoProgramado
from datetime import datetime

# Importa dinámicamente las clases relacionadas con tratamientos para evitar importaciones circulares.
def obtener_tratamiento():
    from tratamiento import Tratamiento, RegistroTratamientos
    return Tratamiento, RegistroTratamientos

class Animal:
    """
    Clase base para representar un animal. Esta clase maneja las características generales
    de un animal, como su nombre, especie, edad y la posibilidad de llevar un registro de
    su cartilla de vacunación, alimentación, cuidados programados y tratamientos.
    """

    def __init__(self, chip, nombre, especie, edad, requiere_cartilla=True, requiere_alimentos=True, requiere_cuidados=True):
        """
        Inicializa los atributos básicos del animal.

        :param chip: Identificador único del animal (chip).
        :param nombre: Nombre del animal.
        :param especie: Especie a la que pertenece el animal.
        :param edad: Edad del animal en años.
        :param requiere_cartilla: Indica si el animal tiene una cartilla de vacunación (por defecto True).
        :param requiere_alimentos: Indica si el animal necesita un catálogo de alimentos (por defecto True).
        :param requiere_cuidados: Indica si el animal necesita cuidados programados (por defecto True).
        """
        self.requiere_alimentos = requiere_alimentos
        self.chip = chip
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.cartilla = CartillaVacunacion() if requiere_cartilla else None
        self.catalogo_alimentos = CatalogoAlimentos() if requiere_alimentos else None
        self.dueno = None
        self.cuidados_programados = [] if requiere_cuidados else []
        self.registro_tratamientos = None  # Inicializamos como None, se asigna cuando es necesario

    def __str__(self):
        """
        Representación en formato string de los atributos principales del animal.
        """
        chip_info = f", Chip: {self.chip}" if self.chip else ""
        dueno_info = f", Dueño: {self.dueno.nombre}" if self.dueno else ""
        cartilla_info = f"\nCartilla de vacunación:\n{self.cartilla}" if self.cartilla else ""
        alimentos_info = f"\nAlimentos:\n {self.catalogo_alimentos}" if self.catalogo_alimentos else ""
        cuidados_info = f"\nCuidados programados:\n{self.mostrar_cuidados()}" if self.cuidados_programados else ""
        base = f"{self.__class__.__name__}: {self.nombre} ({self.especie}, {self.edad} años{chip_info}{dueno_info})"
        return f"{base}{cartilla_info}{alimentos_info}{cuidados_info}"

    def __repr__(self):
        """
        Representación detallada del objeto para propósitos de depuración.
        """
        vacunas_repr = ", ".join(repr(v) for v in self.cartilla.vacunas) if self.cartilla else "no aplica"
        dueno_info = f", dueno_nif={self.dueno.nif!r}" if self.dueno else ""
        return (f"{self.__class__.__name__}(nombre={self.nombre!r}, especie={self.especie!r}, "
                f"edad={self.edad!r}, chip={self.chip!r}, vacunas=[{vacunas_repr}]{dueno_info})")

    def __eq__(self, other):
        """
        Compara dos animales basándose en su chip.
        """
        if not isinstance(other, Animal):
            return False
        return self.chip == other.chip

    def vacunar(self, vacuna):
        """
        Vacuna al animal si tiene una cartilla de vacunación.

        :param vacuna: Nombre de la vacuna.
        """
        try:
            if self.cartilla:
                nueva_vacuna = Vacuna(vacuna, "2025-04-10")
                self.cartilla.agregar_vacuna(nueva_vacuna)
                print(f"{self.nombre} ha sido vacunado con {vacuna}.")
            else:
                raise AttributeError(f"{self.__class__.__name__} no tiene cartilla de vacunación.")
        except AttributeError as e:
            print(f"Error: {e}")

    def alimentar(self, alimento: Alimento):
        """
        Alimenta al animal utilizando el catálogo de alimentos disponible.

        :param alimento: Instancia del alimento que se va a asignar.
        """
        if self.catalogo_alimentos:
            self.catalogo_alimentos.agregar_alimento(alimento)
            print(f"{self.nombre} ha sido alimentado con {alimento.alimento}.")
        else:
            print(f"{self.nombre} no tiene catálogo de alimentos.")

    def asignar_alimentos(self, catalogo):
        """
        Asigna alimentos disponibles a partir de un catálogo según la especie del animal.

        :param catalogo: Lista de alimentos disponibles para asignar.
        """
        if self.catalogo_alimentos:
            alimentos_disponibles = [alimento for alimento in catalogo if alimento.tipo_animal == self.especie.lower()]
            for alimento in alimentos_disponibles:
                self.catalogo_alimentos.agregar_alimento(alimento)
            print(f"Alimentos asignados a {self.nombre}: {', '.join([a.alimento for a in alimentos_disponibles])}")
        else:
            print(f"{self.nombre} no tiene catálogo de alimentos asignado.")

    def asignar_cuidado(self, cuidado: CuidadoProgramado):
        """
        Asigna un cuidado programado al animal.

        :param cuidado: Objeto CuidadoProgramado que define el tipo de cuidado y fecha.
        """
        if self.requiere_cuidados:
            self.cuidados_programados.append(cuidado)
            print(f"{self.nombre} tiene un nuevo cuidado programado: {cuidado.tipo_cuidado} para el {cuidado.fecha.date()}.")
        else:
            print(f"{self.nombre} no requiere cuidados programados.")

    def mostrar_cuidados(self):
        """
        Muestra los cuidados programados del animal.

        :return: Cadena con la lista de cuidados programados.
        """
        if self.cuidados_programados:
            return "\n".join(str(cuidado) for cuidado in self.cuidados_programados)
        else:
            return "  - No hay cuidados programados."

    def aplicar_tratamiento(self, tratamiento):
        """
        Aplica un tratamiento al animal y lo registra.

        :param tratamiento: Objeto Tratamiento que contiene la información sobre el tratamiento.
        """
        Tratamiento, RegistroTratamientos = obtener_tratamiento()  # Importa las clases de tratamiento solo cuando es necesario
        if self.registro_tratamientos is None:
            self.registro_tratamientos = RegistroTratamientos()  # Inicializa el registro de tratamientos si aún no existe

        self.registro_tratamientos.agregar_tratamiento(tratamiento)
        print(f"{self.nombre} ha recibido el tratamiento: {tratamiento.nombre}")


class Perro(Animal):
    """

    Clase que representa un perro, heredando de la clase Animal.

    Clase que representa un perro, heredada de la clase Animal. Un perro tiene una raza además de las
    características comunes de un animal.

    """
    def __init__(self, chip, nombre, edad, raza):
        super().__init__(chip, nombre, "Perro", edad)
        self.raza = raza

    def __str__(self):
        """
        Representación del perro en formato string, con su información básica.
        """
        cartilla_info = f"\nCartilla de vacunación:\n{self.cartilla}" if self.cartilla else ""
        alimentos_info = f"\nAlimentos:\n {self.catalogo_alimentos}" if self.catalogo_alimentos else ""
        return (f"{self.__class__.__name__}: {self.nombre} ({self.especie}, {self.edad} años, "
                f"Raza: {self.raza}, Chip: {self.chip}){cartilla_info}{alimentos_info}")

    def __repr__(self):
        """
        Representación detallada para el perro.
        """
        base = super().__repr__()[:-1]
        return f"{base}, raza={self.raza!r})"


class Gato(Animal):
    """
    Clase que representa un gato, heredando de la clase Animal.
    """
    def __init__(self, chip, nombre, edad, raza):
        super().__init__(chip, nombre, "Gato", edad)
        self.raza = raza

    def __str__(self):
        """
        Representación del gato en formato string.
        """
        cartilla_info = f"\nCartilla de vacunación:\n{self.cartilla}" if self.cartilla else ""
        alimentos_info = f"\nAlimentos:\n {self.catalogo_alimentos}" if self.catalogo_alimentos else ""
        return (f"{self.__class__.__name__}: {self.nombre} ({self.especie}, {self.edad} años, "
                f"Raza: {self.raza}, Chip: {self.chip}){cartilla_info}{alimentos_info}")

    def __repr__(self):
        """
        Representación detallada para el gato.
        """
        base = super().__repr__()[:-1]
        return f"{base}, raza={self.raza!r})"


class Ave(Animal):
    """
    Clase que representa un ave, heredando de la clase Animal.
    """
    def __init__(self, nombre, edad):
        super().__init__(None, nombre, "Ave", edad, requiere_cartilla=False)

    def __str__(self):
        """
        Representación del ave en formato string.
        """
        alimentos_info = f"\nAlimentos:\n {self.catalogo_alimentos}" if self.catalogo_alimentos else ""
        return f"{self.__class__.__name__}: {self.nombre} ({self.especie}, {self.edad} años){alimentos_info}"

    def __repr__(self):
        """
        Representación detallada para el ave.
        """
        base = super().__repr__()[:-1]
        return f"{base})"


class Pez(Animal):
    """
    Clase que representa un pez, heredando de la clase Animal.
    """
    def __init__(self, nombre, edad):
        super().__init__(None, nombre, "Pez", edad, requiere_cartilla=False)

    def __str__(self):
        """
        Representación del pez en formato string.
        """
        alimentos_info = f"\nAlimentos:\n {self.catalogo_alimentos}" if self.catalogo_alimentos else ""
        return f"{self.__class__.__name__}: {self.nombre} ({self.especie}, {self.edad} años){alimentos_info}"

    def __repr__(self):
        """
        Representación detallada para el pez.
        """
        base = super().__repr__()[:-1]
        return f"{base})"  

