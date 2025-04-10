"""
menu_animales.py

Módulo que gestiona la interacción de usuario para crear, listar y administrar
animales (Perro, Gato, Ave, Pez) dentro de la aplicación. NO depende de ninguna
carpeta acceso_datos. Almacena los animales en una lista local en memoria.

Autor: [Tu Nombre]
Fecha: [Fecha Actual]
"""


from animales.animal import Perro, Gato, Ave, Pez


_animales_en_memoria = []

def menu_animales():
    """
    Menú principal para la gestión de animales.

    - Ofrece listar animales
    - Crear un nuevo animal
    - Volver al menú anterior (o principal)

    Retorno
    -------
    None
        Solo imprime menús y llama a otras funciones.
    """
    while True:
        print("\n=== MENÚ DE ANIMALES ===")
        print("1. Listar animales")
        print("2. Registrar nuevo animal")
        print("3. Volver al menú anterior")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == '1':
            listar_animales()
        elif opcion == '2':
            registrar_animal()
        elif opcion == '3':
            print("Volviendo al menú anterior...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

def listar_animales():
    """
    Lista los animales registrados en la variable global _animales_en_memoria.

    - Si la lista está vacía, muestra un mensaje.
    - Si no, muestra cada animal con su índice y la representación
      devuelta por su método __str__ (definido en animal.py).

    Retorno
    -------
    None
    """
    if not _animales_en_memoria:
        print("\nNo hay animales registrados.")
        return

    print("\nAnimales registrados:")
    for idx, animal in enumerate(_animales_en_memoria, start=1):
        print(f"{idx}. {animal}")

def registrar_animal():
    """
    Permite al usuario crear un nuevo animal preguntando:
      - tipo (perro, gato, ave o pez)
      - nombre
      - edad
      - chip y raza (solo para perro o gato)
    
    Crea la instancia correspondiente (Perro, Gato, Ave, Pez) y la
    almacena en la lista _animales_en_memoria.

    Retorno
    -------
    None
    """
    print("\n=== Registrar Nuevo Animal ===")
    tipo = input("Tipo (perro, gato, ave, pez): ").strip().lower()
    nombre = input("Nombre: ").strip()
    edad_str = input("Edad (años): ").strip()

    # Convertir a entero la edad
    try:
        edad = int(edad_str)
    except ValueError:
        print("⚠️ Valor de edad no válido. Se usará 0.")
        edad = 0

    if tipo == "perro":
        raza = input("Raza: ").strip()
        chip = input("Chip (deja vacío si no tiene): ").strip()
        nuevo = Perro(chip, nombre, edad, raza)
    elif tipo == "gato":
        raza = input("Raza: ").strip()
        chip = input("Chip (deja vacío si no tiene): ").strip()
        nuevo = Gato(chip, nombre, edad, raza)
    elif tipo == "ave":
        nuevo = Ave(nombre, edad)
    elif tipo == "pez":
        nuevo = Pez(nombre, edad)
    else:
        print(f"Tipo '{tipo}' no reconocido. Operación cancelada.")
        return

    _animales_en_memoria.append(nuevo)
    print(f"\n✔️ '{nombre}' de tipo '{tipo}' registrado con éxito en memoria.")

# Permite probarlo directamente si lo ejecutamos suelto
if __name__ == "__main__":
    menu_animales()
