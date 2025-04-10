from datetime import datetime
from typing import List, Union

class Alimento:
    """
    Representa un alimento para un animal.

    Atributos:
        tipo_animal (str): Tipo de animal al que está destinado el alimento.
        alimento (str): Nombre del alimento.
        cantidad (int): Cantidad de alimento en gramos.
        fecha_caducidad (str): Fecha de caducidad del alimento (formato string).
        coste (float): Precio del alimento en euros.
    """
    def __init__(self, tipo_animal, alimento, cantidad, fecha_caducidad, coste):
        """
        Inicializa una nueva instancia de Alimento.

        Args:
            tipo_animal (str): Tipo de animal (ej. perro, gato).
            alimento (str): Nombre del alimento.
            cantidad (int): Cantidad en gramos.
            fecha_caducidad (str): Fecha de caducidad (formato string).
            coste (float): Precio en euros.
        """
        self.tipo_animal = tipo_animal
        self.alimento = alimento
        self.cantidad = cantidad
        self.fecha_caducidad = datetime.strptime(fecha_caducidad)
        self.coste = coste

    def __str__(self):
        """
        Devuelve una representación legible del alimento.

        Returns:
            str: Información sobre el alimento.
        """
        return f"{self.alimento} ({self.tipo_animal}) - {self.cantidad}g, caduca el {self.fecha_caducidad}, precio: {self.coste}€"


class CatalogoAlimentos:
    """
    Representa un catálogo de alimentos para animales.

    Atributos:
        alimentos (list): Lista de alimentos disponibles.
    """
    def __init__(self):
        """
        Inicializa un catálogo vacío.
        """
        self.alimentos = []

    def agregar_alimento(self, alimento):
        """
        Agrega un alimento al catálogo.

        Args:
            alimento (Alimento): Instancia de la clase Alimento a agregar.
        """
        self.alimentos.append(alimento)

    def __str__(self):
        """
        Devuelve una representación legible del catálogo de alimentos.

        Returns:
            str: Lista de alimentos o mensaje si está vacío.
        """
        if not self.alimentos:
            return "  - Sin alimentos registrados"
        return "\n".join(f"  - {a}" for a in self.alimentos)
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