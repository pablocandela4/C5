"""
menu_cuidados.py

Proporciona un menú para gestionar los cuidados de los animales:
- Ver cuidados programados
- Añadir un nuevo cuidado
- Realizar (ejecutar) un cuidado
- Volver

Usa clases definidas en cuidados/cuidado_base.py, cuidado_perro.py, etc.
Guarda la información en una lista local '_cuidados'.
"""

from datetime import datetime
from cuidados.cuidado_perro import CuidadoPerro
from cuidados.cuidado_gato import CuidadoGato
from cuidados.cuidado_ave import CuidadoAve
from cuidados.cuidado_pez import CuidadoPez

_cuidados = []

def menu_cuidados():
    """
    Menú principal para la gestión de cuidados:
      1. Ver cuidados programados
      2. Añadir nuevo cuidado
      3. Realizar un cuidado
      4. Volver al menú anterior
    """
    while True:
        print("\n=== MENÚ DE CUIDADOS ===")
        print("1. Ver cuidados programados")
        print("2. Añadir nuevo cuidado")
        print("3. Realizar un cuidado")
        print("4. Volver")

        opcion = input("Selecciona una opción: ").strip()
        if opcion == '1':
            ver_cuidados()
        elif opcion == '2':
            anadir_cuidado()
        elif opcion == '3':
            realizar_cuidado()
        elif opcion == '4':
            print("Volviendo al menú anterior...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

def ver_cuidados():
    """
    Muestra todos los cuidados programados en '_cuidados'.
    Si la lista está vacía, lo notifica.
    """
    if not _cuidados:
        print("\nNo hay cuidados programados.")
        return
    print("\nCuidados programados:")
    for idx, c in enumerate(_cuidados, start=1):
        print(f"{idx}. {c}")  # Usa __str__ (fecha, tipo, estado, etc.)

def anadir_cuidado():
    """
    Permite programar un cuidado para un animal, pidiendo tipo (perro, gato, ave, pez),
    fecha (YYYY-MM-DD), tipo de cuidado (por ejemplo, 'baño perro', 'corte uñas gato', etc.),
    y animal_id (solo si queréis identificar el animal).
    """
    print("\n=== Añadir Cuidado Programado ===")
    especie = input("Especie del animal (perro, gato, ave, pez): ").strip().lower()
    fecha_str = input("Fecha (YYYY-MM-DD): ").strip()
    tipo_cuidado = input("Tipo de cuidado: ").strip()
    animal_id_str = input("ID del animal (si usáis un identificador numérico): ").strip()

    # Convertir la fecha a un formato válido si queréis validarla, aquí vamos simple.
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
    except ValueError:
        print("Fecha inválida, se usará hoy.")
        fecha_str = datetime.now().strftime("%Y-%m-%d")

    if not animal_id_str.isdigit():
        animal_id_str = "0"  # Por si no tenéis ID

    # Creamos la subclase adecuada
    if especie == "perro":
        nuevo = CuidadoPerro(fecha_str, tipo_cuidado, animal_id=animal_id_str)
    elif especie == "gato":
        nuevo = CuidadoGato(fecha_str, tipo_cuidado, animal_id=animal_id_str)
    elif especie == "ave":
        nuevo = CuidadoAve(fecha_str, tipo_cuidado, animal_id=animal_id_str)
    elif especie == "pez":
        nuevo = CuidadoPez(fecha_str, tipo_cuidado, animal_id=animal_id_str)
    else:
        print(f"Especie '{especie}' no reconocida. Operación cancelada.")
        return

    _cuidados.append(nuevo)
    print(f"Se ha programado el cuidado '{tipo_cuidado}' para el {fecha_str}.")

def realizar_cuidado():
    """
    Permite seleccionar un cuidado de la lista y ejecutar su método 'realizar_cuidado()'.
    Actualiza el estado a 'realizado' o similar.
    """
    if not _cuidados:
        print("No hay cuidados programados.")
        return

    ver_cuidados()
    try:
        idx_str = input("\nSelecciona el número del cuidado a realizar: ")
        idx = int(idx_str)
        if idx < 1 or idx > len(_cuidados):
            print("Índice fuera de rango.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    cuidado = _cuidados[idx - 1]
    cuidado.realizar_cuidado()  # Llama al método de la subclase (CuidadoPerro/Gato/etc.)
    
    cuidado.actualizar_estado("realizado")
    print(f"Estado del cuidado actualizado a 'realizado'.")

if __name__ == "__main__":
    
    menu_cuidados()
