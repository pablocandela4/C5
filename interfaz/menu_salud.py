"""
menu_salud.py

Proporciona un menú para gestionar la salud de los animales:
- Ver vacunas
- Añadir vacunas
- Ver tratamientos
- Añadir tratamientos
- Volver al menú anterior

Guarda los datos en listas locales en memoria:
- _vacunas_registradas
- _tratamientos_registrados
"""

from salud.vacunacion import Vacuna
from salud.tratamiento import Tratamiento

_vacunas_registradas = []
_tratamientos_registrados = []

def menu_salud():
    """
    Menú de gestión de salud (vacunas, tratamientos).
    Ofrece las siguientes opciones:
      1. Ver vacunas
      2. Añadir vacuna
      3. Ver tratamientos
      4. Añadir tratamiento
      5. Volver
    """
    while True:
        print("\n=== MENÚ DE SALUD ===")
        print("1. Ver vacunas")
        print("2. Añadir vacuna")
        print("3. Ver tratamientos")
        print("4. Añadir tratamiento")
        print("5. Volver al menú anterior")

        opcion = input("Selecciona una opción: ").strip()
        if opcion == '1':
            ver_vacunas()
        elif opcion == '2':
            anadir_vacuna()
        elif opcion == '3':
            ver_tratamientos()
        elif opcion == '4':
            anadir_tratamiento()
        elif opcion == '5':
            print("Volviendo al menú anterior...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

def ver_vacunas():
    """
    Muestra todas las vacunas registradas.
    Si la lista está vacía, lo notifica.
    """
    if not _vacunas_registradas:
        print("\nNo hay vacunas registradas.")
        return
    print("\nVacunas registradas:")
    for idx, v in enumerate(_vacunas_registradas, start=1):
        print(f"{idx}. {v}")  # Usa el __str__ de Vacuna

def anadir_vacuna():
    """
    Pide al usuario los datos de una vacuna (nombre, fecha) y la añade a la lista local.
    """
    print("\n=== Añadir Vacuna ===")
    nombre = input("Nombre de la vacuna: ").strip()
    fecha = input("Fecha de administración (YYYY-MM-DD): ").strip()

    nueva = Vacuna(nombre, fecha)
    _vacunas_registradas.append(nueva)
    print(f"Vacuna '{nombre}' añadida con fecha {fecha}.")

def ver_tratamientos():
    """
    Muestra todos los tratamientos registrados.
    Si la lista está vacía, lo notifica.
    """
    if not _tratamientos_registrados:
        print("\nNo hay tratamientos registrados.")
        return
    print("\nTratamientos registrados:")
    for idx, t in enumerate(_tratamientos_registrados, start=1):
        print(f"{idx}. {t}")  # Usa el __str__ de Tratamiento

def anadir_tratamiento():
    """
    Pide al usuario los datos de un tratamiento (nombre, fecha inicio/fin, coste)
    y lo añade a la lista local.
    """
    print("\n=== Añadir Tratamiento ===")
    nombre = input("Nombre del tratamiento: ").strip()
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
    fecha_fin = input("Fecha de fin (YYYY-MM-DD): ").strip()
    coste_str = input("Coste (€): ").strip()
    try:
        coste = float(coste_str)
    except ValueError:
        print("Coste inválido. Se usará 0.0")
        coste = 0.0

    nuevo = Tratamiento(nombre, fecha_inicio, fecha_fin, coste)
    _tratamientos_registrados.append(nuevo)
    print(f"Tratamiento '{nombre}' añadido correctamente.")

if __name__ == "__main__":
    
    menu_salud()
