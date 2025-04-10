"""
gestor_salud.py

Contiene funciones para gestionar vacunas y tratamientos: guardar, cargar y mostrar.

Funciones:
    guardar_vacunas(cartilla, archivo): Guarda las vacunas en un archivo CSV.
    cargar_vacunas(archivo): Carga las vacunas desde un archivo CSV y devuelve una lista de objetos Vacuna.
    guardar_tratamientos(lista_tratamientos, archivo): Guarda los tratamientos en un archivo CSV.
    cargar_tratamientos(archivo): Carga tratamientos desde un archivo CSV y devuelve una lista de objetos Tratamiento.
"""

import csv
from vacunacion import Vacuna, CartillaVacunacion
from tratamiento import Tratamiento, RegistroTratamientos


def guardar_vacunas(cartilla, file='datos/vacunas.csv'):
    """
    Guarda una lista de vacunas en un archivo CSV.

    Args:
        cartilla (CartillaVacunacion): Objeto con lista de vacunas.
        file (str): Ruta del archivo donde se guardará la información.
    """
    with open(file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["nombre", "fecha"])
        for v in cartilla.vacunas:
            writer.writerow([v.nombre, v.fecha])


def cargar_vacunas(file='datos/vacunas.csv'):
    """
    Carga las vacunas desde un archivo CSV.

    Args:
        file (str): Ruta del archivo desde el cual se cargará la información.

    Returns:
        CartillaVacunacion: Cartilla con las vacunas cargadas.
    """
    cartilla = CartillaVacunacion()
    try:
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                vacuna = Vacuna(nombre=row["nombre"], fecha=row["fecha"])
                cartilla.agregar_vacuna(vacuna)
    except FileNotFoundError:
        print(f'Archivo {file} no encontrado.')
    return cartilla


def guardar_tratamientos(registro, file='datos/tratamientos.csv'):
    """
    Guarda una lista de tratamientos en un archivo CSV.

    Args:
        registro (ListaTratamientos): Objeto con lista de tratamientos.
        file (str): Ruta del archivo donde se guardará la información.
    """
    with open(file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["nombre", "fecha_inicio", "fecha_fin", "coste"])
        for t in registro.tratamientos:
            writer.writerow([t.nombre, t.fecha_inicio, t.fecha_fin, f'{t.coste:.2f}'])


def cargar_tratamientos(file='datos/tratamientos.csv'):
    """
    Carga los tratamientos desde un archivo CSV.

    Args:
        file (str): Ruta del archivo desde el cual se cargará la información.

    Returns:
        ListaTratamientos: Objeto con los tratamientos cargados.
    """
    registro = RegistroTratamientos()
    try:
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tratamiento = Tratamiento(
                    nombre=row["nombre"],
                    fecha_inicio=row["fecha_inicio"],
                    fecha_fin=row["fecha_fin"],
                    coste=float(row["coste"])
                )
                registro.agregar_tratamiento(tratamiento)
    except FileNotFoundError:
        print(f'Archivo {file} no encontrado.')
    return registro
