"""
menu_principal.py

Menú principal de la aplicación de la clínica veterinaria.

Ofrece acceso a los submenús:
    - Animales
    - Salud
    - Alimentación
    - Cuidados

Autor: Lucas Beneyto
"""

import sys

from .menu_animales import menu_animales
from .menu_salud import menu_salud
from .menu_alimentacion import menu_alimentacion
from .menu_cuidados import menu_cuidados

def menu_principal():
    """
    Muestra el menú principal del programa.

    Opciones:
        1. Ir al menú de animales
        2. Ir al menú de salud
        3. Ir al menú de alimentación
        4. Ir al menú de cuidados
        5. Salir

    Retorno
    -------
    None
        Solo imprime opciones y gestiona el bucle principal hasta
        que el usuario elige salir.
    """
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestión de Animales")
        print("2. Gestión de Salud (vacunas, tratamientos)")
        print("3. Gestión de Alimentación")
        print("4. Gestión de Cuidados")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == '1':
            menu_animales()
        elif opcion == '2':
            menu_salud()
        elif opcion == '3':
            menu_alimentacion()
        elif opcion == '4':
            menu_cuidados()
        elif opcion == '5':
            print("Saliendo de la aplicación... ¡Hasta la próxima!")
            sys.exit(0)
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    
    menu_principal()
