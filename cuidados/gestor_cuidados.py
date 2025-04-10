"""
gestor_cuidados.py

Contiene funciones para gestionar cuidados programados: guardar, cargar, mostrar, buscar y cambiar estado.

Funciones:
    guardar_cuidados(lista_cuidados, archivo): Guarda una lista de cuidados en un archivo CSV.
    cargar_cuidados(archivo): Carga cuidados desde un archivo CSV y los devuelve como una lista de objetos.
    mostrar_cuidados(lista_cuidados): Imprime todos los cuidados en pantalla.
    buscar_cuidados_por_animal(lista, animal_id): Devuelve una lista de cuidados para un animal específico.
    cambiar_estado_cuidado(cuidado, nuevo_estado): Actualiza el estado de un cuidado.
"""

import csv
from .cuidado_perro import CuidadoPerro
from .cuidado_gato import CuidadoGato
from .cuidado_ave import CuidadoAve
from .cuidado_pez import CuidadoPez
from .cuidado_base import CuidadoProgramado

def guardar_cuidados(lista_cuidados, archivo="datos/cuidados.csv"):
    """
    Guarda una lista de cuidados en un archivo CSV.

    Args:
        lista_cuidados (list): Lista de objetos que heredan de CuidadoProgramado.
        archivo (str): Ruta del archivo donde se guardará la información.
    """
    with open(archivo, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["animal_id", "fecha", "tipo_cuidado", "estado", "notas"])
        for c in lista_cuidados:
            writer.writerow([c.animal_id, c.fecha.date(), c.tipo_cuidado, c.estado, c.notas])

def cargar_cuidados(archivo="datos/cuidados.csv"):
    """
    Carga los cuidados desde un archivo CSV y los devuelve como una lista de objetos.

    Args:
        archivo (str): Ruta del archivo desde el cual se cargará la información.

    Returns:
        list: Lista de objetos de tipo CuidadoProgramado o derivados.
    """
    cuidados = []
    clase_por_tipo = {
        "perro": CuidadoPerro,
        "gato": CuidadoGato,
        "ave": CuidadoAve,
        "pez": CuidadoPez
    }
    try:
        with open(archivo, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tipo = row["tipo_cuidado"].lower()
                clase = clase_por_tipo.get(tipo.split()[0], CuidadoProgramado)
                cuidado = clase(
                    fecha=row["fecha"],
                    tipo_cuidado=row["tipo_cuidado"],
                    estado=row["estado"],
                    notas=row["notas"],
                    animal_id=row["animal_id"]
                )
                cuidados.append(cuidado)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {archivo}")
    return cuidados

def mostrar_cuidados(lista_cuidados):
    """
    Muestra por pantalla todos los cuidados presentes en la lista.

    Args:
        lista_cuidados (list): Lista de objetos de tipo CuidadoProgramado.
    """
    for c in lista_cuidados:
        print(c)

def buscar_cuidados_por_animal(lista, animal_id):
    """
    Busca los cuidados asignados a un animal específico por su ID.

    Args:
        lista (list): Lista de objetos de tipo CuidadoProgramado.
        animal_id (int): Identificador del animal.

    Returns:
        list: Lista de cuidados que coinciden con el animal_id.
    """
    return [c for c in lista if str(c.animal_id) == str(animal_id)]

def cambiar_estado_cuidado(cuidado, nuevo_estado):
    """
    Cambia el estado de un cuidado a un nuevo valor.

    Args:
        cuidado (CuidadoProgramado): Objeto de cuidado a modificar.
        nuevo_estado (str): Nuevo estado ('pendiente', 'realizado', 'cancelado').
    """
    try:
        cuidado.actualizar_estado(nuevo_estado)
        print("Estado actualizado correctamente.")
    except ValueError as e:
        print(f"Error: {e}")