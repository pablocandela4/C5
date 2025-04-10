from alimentacion import Alimento

def comprar_alimento():
    """Solicita al usuario el tipo de animal para el que desea comprar alimento.

    Returns
    -------
    str
        El tipo de animal seleccionado por el usuario en minúsculas.
    """
    animales = ['perro', 'gato', 'ave', 'pez']
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

    def __init__(self, catalogo):
        """Inicializa un objeto Venta con un catálogo de alimentos.

        Parameters
        ----------
        catalogo : List[Alimento]
            Lista de objetos Alimento que representan los productos disponibles.
        """
        self.catalogo = catalogo
        self.carrito = []

    def mostrar_productos(self, tipo_animal):
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
        tipo_animal = comprar_alimento()  # esta función la definimos arriba
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