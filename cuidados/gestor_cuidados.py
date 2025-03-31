import csv

def guardar_cuidados(lista_cuidados, archivo="datos/cuidados.csv"):
    """
    Guarda una lista de cuidados en un archivo CSV.

    Args:
        lista_cuidados (list): Lista de objetos que heredan de CuidadoProgramado.
        archivo (str): Ruta del archivo donde guardar los datos.
    """
    with open(archivo, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["animal_id", "fecha", "tipo_cuidado", "estado", "notas"])
        for c in lista_cuidados:
            writer.writerow([c.animal_id, c.fecha.date(), c.tipo_cuidado, c.estado, c.notas])

def mostrar_cuidados(lista_cuidados):
    """
    Muestra por pantalla los cuidados de una lista.

    Args:
        lista_cuidados (list): Lista de objetos de tipo CuidadoProgramado o similar.
    """
    for c in lista_cuidados:
        print(c)
