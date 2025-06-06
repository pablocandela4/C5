import csv
import os
from alimentacion import *

historial = "historial.csv"

class Historial:
    """Clase para gestionar el historial de catálogo y ventas de alimentos en un archivo CSV.
    Attributes
    ----------
    archivo : str
        La ruta del archivo CSV donde se guarda el historial (por defecto "historial.csv").
    """
    def __init__(self, archivo=historial):
        """Inicializa un objeto Historial con un archivo CSV.
        Parameters
        ----------
        archivo : str, optional
            La ruta del archivo CSV donde se almacenará el historial (por defecto "historial.csv").
        """
        self.archivo = archivo
        if not os.path.isfile(self.archivo):
            self.crear_archivo()

    def crear_archivo(self):
        """Crea el archivo historial.csv con encabezados si no existe."""
        with open(self.archivo, mode='w', newline='') as archivo:
            archivo.write("--- CATÁLOGO DE ALIMENTOS ---\n")
            writer = csv.writer(archivo)
            writer.writerow(["Tipo Animal", "Alimento", "Cantidad (g)", "Fecha de Caducidad", "Coste (€)"])
            archivo.write("\n--- HISTORIAL DE VENTAS ---\n")
            writer.writerow(["Tipo Animal", "Alimento", "Cantidad (g)", "Fecha de Caducidad", "Coste (€)"])
        print(" Archivo historial.csv creado correctamente.")

    def guardar_alimentos(self, catalogo):
        """Guarda el catálogo de alimentos en el archivo historial.csv.
        Parameters
        ----------
        catalogo : list[Alimento]
            Lista de objetos Alimento que representan el catálogo a guardar.
        """
        with open(self.archivo, mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            for alimento in catalogo:
                writer.writerow([
                    alimento.tipo_animal,
                    alimento.alimento,
                    alimento.cantidad,
                    alimento.fecha_caducidad.date(),
                    f"{alimento.coste:.2f}"
               ])

    def guardar_ventas(self, carrito):
        """Agrega productos vendidos al final del historial.csv bajo el apartado de ventas.
        Parameters
        ----------
        carrito : list[Alimento]
            Lista de objetos Alimento que representan los productos vendidos.
        """
        with open(self.archivo, 'a', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            for producto in carrito:
                writer.writerow([
                    producto.tipo_animal,
                    producto.alimento,
                    producto.cantidad,
                    producto.fecha_caducidad.date(),
                    f"{producto.coste:.2f}"
                ])
