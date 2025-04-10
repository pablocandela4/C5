"""
menu_alimentacion.py

Proporciona un menú para gestionar la alimentación de animales:
- Ver alimentos disponibles
- Añadir alimentos
- Mostrar "carrito" de compras
- Añadir un alimento al carrito
- Volver

Guarda en listas locales:
- _catalogo_alimentos
- _carrito
"""

from alimentacion.alimentacion import Alimento

_catalogo_alimentos = []
_carrito = []

def menu_alimentacion():
    """
    Menú de gestión de alimentación:
      1. Ver alimentos disponibles
      2. Añadir alimento al catálogo
      3. Ver carrito de compra
      4. Añadir alimento al carrito
      5. Volver al menú anterior
    """
    while True:
        print("\n=== MENÚ DE ALIMENTACIÓN ===")
        print("1. Ver alimentos disponibles")
        print("2. Añadir alimento al catálogo")
        print("3. Ver carrito")
        print("4. Añadir alimento al carrito")
        print("5. Volver")

        opcion = input("Selecciona una opción: ").strip()
        if opcion == '1':
            ver_alimentos()
        elif opcion == '2':
            anadir_alimento()
        elif opcion == '3':
            ver_carrito()
        elif opcion == '4':
            anadir_alimento_al_carrito()
        elif opcion == '5':
            print("Volviendo al menú anterior...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

def ver_alimentos():
    """
    Muestra todos los alimentos del catálogo local.
    Si la lista está vacía, lo notifica.
    """
    if not _catalogo_alimentos:
        print("\nNo hay alimentos en el catálogo.")
        return
    print("\nCatálogo de alimentos:")
    for idx, ali in enumerate(_catalogo_alimentos, start=1):
        print(f"{idx}. {ali}")  # Usa el __str__ de Alimento

def anadir_alimento():
    """
    Pide datos para crear un nuevo Alimento y lo añade al catálogo local.
    """
    print("\n=== Añadir Alimento al Catálogo ===")
    tipo_animal = input("Tipo de animal: ").strip().lower()
    nombre_alimento = input("Nombre del alimento: ").strip()
    cantidad_str = input("Cantidad (gramos): ").strip()
    fecha_caducidad = input("Fecha de caducidad (YYYY-MM-DD): ").strip()
    coste_str = input("Coste (€): ").strip()

    try:
        cantidad = int(cantidad_str)
    except ValueError:
        print("Cantidad inválida, se usará 0.")
        cantidad = 0

    try:
        coste = float(coste_str)
    except ValueError:
        print("Coste inválido, se usará 0.0.")
        coste = 0.0

    nuevo = Alimento(tipo_animal, nombre_alimento, cantidad, fecha_caducidad, coste)
    _catalogo_alimentos.append(nuevo)
    print(f"Alimento '{nombre_alimento}' para '{tipo_animal}' añadido al catálogo.")

def ver_carrito():
    """
    Muestra el contenido actual del carrito.
    Si está vacío, lo notifica.
    """
    if not _carrito:
        print("\nEl carrito está vacío.")
        return
    print("\nCarrito de compras:")
    for idx, prod in enumerate(_carrito, start=1):
        print(f"{idx}. {prod}")  # Usa __str__ de Alimento

def anadir_alimento_al_carrito():
    """
    Permite seleccionar un alimento del catálogo y añadirlo al carrito.
    """
    if not _catalogo_alimentos:
        print("No hay alimentos en el catálogo.")
        return
    ver_alimentos()
    try:
        opcion = int(input("\nSelecciona el número del alimento que deseas añadir al carrito: "))
        if opcion < 1 or opcion > len(_catalogo_alimentos):
            raise ValueError
    except ValueError:
        print("Opción no válida.")
        return

    producto = _catalogo_alimentos[opcion - 1]
    _carrito.append(producto)
    print(f"'{producto.alimento}' añadido al carrito.")

if __name__ == "__main__":
   
    
    menu_alimentacion()
