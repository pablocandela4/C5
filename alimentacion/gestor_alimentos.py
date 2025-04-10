import csv
import os
from alimentacion import Alimento

GESTOR_ARCHIVO = "gestor_alimentos.csv"

class Gestor:
    """
    Clase para gestionar el historial de catálogo y ventas de alimentos en un archivo CSV.

    Atributos
    ----------
    archivo : str
        Ruta del archivo CSV que se utilizará para guardar la información.
    """

    def __init__(self, archivo=GESTOR_ARCHIVO):
        """
        Inicializa un objeto Gestor con el archivo de gestión.

        Parámetros
        ----------
        archivo : str, opcional
            Ruta del archivo a usar (por defecto 'gestor_alimentos.csv').
        """
        self.archivo = archivo
        if not os.path.isfile(self.archivo):
            self.crear_archivo()

    def crear_archivo(self):
        """
        Crea el archivo CSV inicial con secciones para el catálogo y el historial de ventas.
        """
        with open(self.archivo, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["--- CATÁLOGO DE ALIMENTOS ---"])
            writer.writerow(["Tipo Animal", "Alimento", "Cantidad (g)", "Fecha de Caducidad", "Coste (€)"])
            writer.writerow(["--- FIN CATÁLOGO ---"])
            writer.writerow(["--- HISTORIAL DE VENTAS ---"])
            writer.writerow(["Tipo Animal", "Alimento", "Cantidad (g)", "Fecha de Caducidad", "Coste (€)"])
        print("Archivo gestor_alimentos.csv creado correctamente.")

    def guardar_alimentos(self, catalogo):
        """
        Guarda el catálogo de alimentos en la sección correspondiente del archivo CSV.

        Parámetros
        ----------
        catalogo : list[Alimento]
            Lista de alimentos a guardar.
        """
        with open(self.archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()

        fin_catalogo_index = None
        for i, linea in enumerate(lineas):
            if "--- FIN CATÁLOGO ---" in linea:
                fin_catalogo_index = i
                break

        if fin_catalogo_index is None:
            print("No se encontró el marcador de fin de catálogo.")
            return

        nuevas_lineas = []
        for alimento in catalogo:
            nuevas_lineas.append(f"{alimento.tipo_animal},{alimento.alimento},{alimento.cantidad},{alimento.fecha_caducidad},{alimento.coste:.2f}\n")

        lineas = lineas[:fin_catalogo_index] + nuevas_lineas + lineas[fin_catalogo_index:]

        with open(self.archivo, 'w', encoding='utf-8') as f:
            f.writelines(lineas)

    def guardar_ventas(self, carrito):
        """
        Agrega los productos vendidos a la sección de historial de ventas del archivo CSV.

        Parámetros
        ----------
        carrito : list[Alimento]
            Lista de productos vendidos.
        """
        with open(self.archivo, mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            for producto in carrito:
                writer.writerow([
                    producto.tipo_animal,
                    producto.alimento,
                    producto.cantidad,
                    producto.fecha_caducidad,
                    f"{producto.coste:.2f}"
                ])

    def mostrar_gestion(self):
        """
        Muestra el contenido completo del archivo de gestión.
        """
        if not os.path.exists(self.archivo):
            print("El archivo no existe.")
            return

        with open(self.archivo, mode='r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print(contenido)

