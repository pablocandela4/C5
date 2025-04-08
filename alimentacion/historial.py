import csv
from datetime import datetime
class Historial:
    def __init__(self):
        self.historial = []

    def agregar(self, categoria, data):
        """Agrega un nuevo registro al historial para la categoría correspondiente."""
        record = {
            "categoria": categoria,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            **data  # Los datos adicionales como alimentación, vacuna, tratamiento, etc.
        }
        self.historial.append(record)
        self.guardar_csv()

    def guardar_csv(self, archivo="historial.csv"):
        """Guarda el historial completo en el archivo CSV."""
        with open(archivo, mode='w', newline='', encoding='utf-8') as file:
            # Especificar los campos que se guardarán en el CSV
            campos = ["categoria", "fecha", "detalle"]
            writer = csv.DictWriter(file, fieldnames=campos)

            # Escribir encabezado si el archivo está vacío
            writer.writeheader()

            # Escribir los registros del historial
            for record in self.historial:
                writer.writerow(record)

    def cargar_csv(self, archivo="historial.csv"):
        """Carga el historial desde un archivo CSV existente."""
        try:
            with open(archivo, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.historial.append(row)
        except FileNotFoundError:
            print(f"[INFO] Archivo {archivo} no encontrado. Comenzando con historial vacío.")

    def mostrar(self):
        if not self.historial:
            print("No hay registros en el historial.")
        else:
            for i, record in enumerate(self.historial, 1):
                print(f"Registro {i}:")
                print(f"  Categoría: {record['categoria']}")
                print(f"  Fecha: {record['fecha']}")
                print(f"  Detalle: {record['detalle']}")
                print("=" * 30)


# Ejemplo de uso con alimentación, vacunas, y tratamientos
if __name__ == "__main__":
    historial = Historial()
    historial.cargar_csv()  # Carga el historial de un archivo CSV existente si lo hay.

    # Agregar un nuevo alimento
    historial.agregar(
        categoria="alimentación",
        data={"detalle": "Comida para perro marca XYZ, 500g, 3€/kg"}
    )

    # Agregar una nueva vacuna
    historial.agregar(
        categoria="vacunas",
        data={"detalle": "Vacuna contra rabia, fecha: 2025-04-01"}
    )

    # Agregar un nuevo tratamiento
    historial.agregar(
        categoria="tratamiento",
        data={"detalle": "Tratamiento para pulgas, 30 días"}
    )

    # Mostrar el historial cargado
