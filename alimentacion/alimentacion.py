from datetime import datetime
from typing import List, Union

class Alimento:
    """Clase utilizada para representar un tipo de alimento para animales.
    Atributos
    ----------
    tipo_animal : str
        El tipo de animal para el que está destinado el alimento (por ejemplo, "perro", "gato").
    alimento : str
        El nombre del producto alimenticio.
    cantidad : int
        La cantidad del alimento en gramos.
    fecha_caducidad : datetime
        La fecha de caducidad del alimento.
    coste : float
        El coste del alimento en euros.
    """
    def __init__(self, tipo_animal: str, alimento: str, cantidad: int, fecha_caducidad: str, coste: Union[int, float]):
        """Inicializa un objeto Alimento con los detalles del alimento.
        Parameters
        ----------
        tipo_animal : str
            El tipo de animal para el que está destinado el alimento.
        alimento : str
            El nombre del producto alimenticio.
        cantidad : int
            La cantidad del alimento en gramos.
        fecha_caducidad : str
            La fecha de caducidad en formato "YYYY-MM-DD".
        coste : Union[int, float]
            El coste del alimento, puede ser un entero o un flotante (se convierte a float).
        """
        self.tipo_animal = tipo_animal
        self.alimento = alimento
        self.cantidad = cantidad  # en gramos
        self.fecha_caducidad = datetime.strptime(fecha_caducidad, "%Y-%m-%d")
        self.coste = float(coste)

    def __repr__(self) -> str:
        """Devuelve una representación en cadena del objeto Alimento.
        Returns
        -------
        str
            Una cadena que describe el tipo, nombre, cantidad, fecha de caducidad y coste del alimento.
        """
        return (
            f"Tipo: {self.tipo_animal} | "
            f"Alimento: {self.alimento} | {self.cantidad} gramos | "
            f"Datos: caduca en {self.fecha_caducidad.date()} y tiene un coste de {self.coste}€ | "
        )

class ListaAlimentos:
    """Clase para gestionar una lista de alimentos para animales.
    Attributes
    ----------
    alimentos : List[Alimento]
        Una lista que contiene objetos de la clase Alimento.
    """

    def __init__(self):
        """Inicializa un objeto ListaAlimentos con una lista vacía."""
        self.alimentos: List[Alimento] = []

    def __str__(self) -> str:
        """Devuelve una representación en cadena del estado de la lista de alimentos.

        Returns
        -------
        str
            Una cadena que indica el número total de alimentos registrados o un mensaje si está vacía.
        """
        if not self.alimentos:
            return " ¡Sin alimentos registrados!"
        return f" Total de {len(self.alimentos)} alimentos registrados"

    def agregar_alimento(self, alimento: Alimento) -> None:
        """Agrega un alimento a la lista.

        Parameters
        ----------
        alimento : Alimento
            El objeto Alimento que se desea agregar a la lista.
        """
        self.alimentos.append(alimento)

    def __getitem__(self, index: int) -> Alimento:
        """Permite acceder a un alimento específico en la lista por su índice.

        Parameters
        ----------
        index : int
            El índice del alimento que se desea obtener.

        Returns
        -------
        Alimento
            El objeto Alimento en la posición especificada.
        """
        return self.alimentos[index]

    def __add__(self, otro: 'ListaAlimentos') -> 'ListaAlimentos':
        """Combina dos objetos ListaAlimentos en uno nuevo.

        Parameters
        ----------
        otro : ListaAlimentos
            Otro objeto ListaAlimentos que se combinará con el actual.

        Returns
        -------
        ListaAlimentos
            Un nuevo objeto ListaAlimentos con los alimentos de ambos combinados.
        """
        nuevo = ListaAlimentos()
        nuevo.alimentos = self.alimentos + otro.alimentos
        return nuevo

    def __iadd__(self, otro: 'ListaAlimentos') -> 'ListaAlimentos':
        """Agrega los alimentos de otro ListaAlimentos al actual.

        Parameters
        ----------
        otro : ListaAlimentos
            Otro objeto ListaAlimentos cuyos alimentos se añadirán al actual.

        Returns
        -------
        ListaAlimentos
            El objeto actual con los alimentos combinados.
        """
        self.alimentos += otro.alimentos
        return self


catalogo = [
    # Perro
    Alimento("perro", "Croquetas Premium", 25, "2025-12-31", 10),
    Alimento("perro", "Carne Seca", 18, "2025-11-15", 8),
    # Gato
    Alimento("gato", "Pescado Seco", 15, "2025-10-10", 5),
    Alimento("gato", "Paté Felino", 20, "2025-12-01", 12),
    # Pez
    Alimento("pez", "Alimento Flotante", 12, "2025-09-30", 15),
    Alimento("pez", "Escamas Tropicales", 9, "2025-11-20", 20),
    # Ave
    Alimento("ave", "Semillas Mixtas", 8, "2025-12-15", 20),
    Alimento("ave", "Barritas Frutales", 11, "2025-10-25", 10),
]

animales = ['perro', 'gato', 'ave', 'pez']

def comprar_alimento():
    """Solicita al usuario el tipo de animal para el que desea comprar alimento.

    Returns
    -------
    str
        El tipo de animal seleccionado por el usuario en minúsculas.
    """
    print("Animales disponibles:", ", ".join(animales))
    animal = input("¿Para qué animal quieres comprar alimento? ").lower()
    while animal not in animales:
        print("Animal no válido. Intenta de nuevo.")
        animal = input("¿Para qué animal quieres comprar alimento? ").lower()
    return animal

class Venta:
    """Una clase para gestionar la venta de alimentos para animales.

    Attributes
    ----------
    catalogo : List[Alimento]
        Lista de alimentos disponibles para la venta.
    carrito : List[Alimento]
        Lista de alimentos seleccionados por el usuario para comprar.
    """

    def __init__(self, catalogo: List[Alimento]):
        """Inicializa un objeto Venta con un catálogo de alimentos.

        Parameters
        ----------
        catalogo : List[Alimento]
            Lista de objetos Alimento que representan los productos disponibles.
        """
        self.catalogo = catalogo
        self.carrito: List[Alimento] = []

    def mostrar_productos(self, tipo_animal: str):
        """Muestra los productos disponibles para un tipo de animal específico.

        Parameters
        ----------
        tipo_animal : str
            El tipo de animal para el que se quieren mostrar los productos.

        Returns
        -------
        List[Alimento]
            Lista de alimentos disponibles para el tipo de animal especificado.
        """
        productos_disponibles = [
            alimento for alimento in self.catalogo if alimento.tipo_animal == tipo_animal
        ]
        print(f"\nProductos disponibles para {tipo_animal}:")
        for idx, producto in enumerate(productos_disponibles):
            print(f"{idx + 1}. {producto}")
        return productos_disponibles

    def realizar_compra(self):
        """Permite al usuario seleccionar y comprar un producto del catálogo."""
        tipo_animal = comprar_alimento()
        productos = self.mostrar_productos(tipo_animal)
        try:
            opcion = int(input("Elige el número del producto que deseas comprar: "))
            while opcion < 1 or opcion > len(productos):
                print("Opción no válida.")
                opcion = int(input("Elige el número del producto que deseas comprar: "))
        except ValueError:
            print("Entrada inválida. Introduce un número.")
            return

        producto_seleccionado = productos[opcion - 1]
        self.carrito.append(producto_seleccionado)
        print(f"\n Has comprado: {producto_seleccionado.alimento} para {producto_seleccionado.tipo_animal}")