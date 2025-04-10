import csv
from datetime import datetime
from animal import Perro, Gato, Ave, Pez
from vacunacion import Vacuna
from alimentacion import Alimento
from cuidado_base import CuidadoProgramado



def obtener_tratamiento():
    from tratamiento import Tratamiento
    return Tratamiento


def obtener_datos_animales(animales):
    """
    Obtiene los datos necesarios de los animales en formato de diccionario
    para luego ser escritos en el archivo CSV.
    """
    datos = []
    for animal in animales:

        info_animal = {
            "Nombre": animal.nombre,
            "Especie": animal.especie,
            "Edad": animal.edad,
            "Chip": animal.chip if animal.chip else "N/A",
            "Raza": getattr(animal, "raza", "N/A"),
            "Vacunas": ", ".join(
                [vacuna.nombre for vacuna in animal.cartilla.vacunas]) if animal.cartilla else "Ninguna",
            "Alimentos": ", ".join([alimento.alimento for alimento in
                                    animal.catalogo_alimentos.alimentos]) if animal.catalogo_alimentos else "Ninguno",
            "Cuidados Programados": ", ".join([cuidado.tipo_cuidado for cuidado in
                                               animal.cuidados_programados]) if animal.cuidados_programados else "Ninguno",
            "Tratamientos": ", ".join([tratamiento.nombre for tratamiento in
                                       animal.registro_tratamientos.tratamientos]) if animal.registro_tratamientos else "Ninguno"
        }
        datos.append(info_animal)
    return datos


def guardar_datos_csv(animales, nombre_archivo="animales.csv"):
    """
    Guarda la información de una lista de animales en un archivo CSV. Los datos incluyen
    nombre, especie, edad, chip, raza, vacunas, alimentos, cuidados programados y tratamientos.

    :param animales: Lista de animales (instancias de Animal y sus subclases)
    :param nombre_archivo: Nombre del archivo CSV donde se guardarán los datos (por defecto "animales.csv")
    """
    datos_animales = obtener_datos_animales(animales)


    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ["Nombre", "Especie", "Edad", "Chip", "Raza", "Vacunas", "Alimentos", "Cuidados Programados",
                  "Tratamientos"]

        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos_animales)

    print(f"Los datos de los animales han sido guardados en el archivo '{nombre_archivo}'.")






