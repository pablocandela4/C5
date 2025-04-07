import csv
from datetime import datetime
from animales import Animal

class Alimentacion:
    def __init__(self, ):
        self.historial = []

    def mostrar(self):
        for i, comida in enumerate(self.historial, 1):
            print(f"{i}. {comida['tipo_comida']} ({comida['marca']}) | {comida['cantidad']}g | "
                  f"Compra: {comida['fecha_compra'].date()} | Caduca: {comida['fecha_caducidad'].date()} | "
                  f"{comida['coste']}€ en {comida['lugar_compra']}")


    @staticmethod
    def anyadir(self, tipo_comida, marca, cantidad, fecha_compra, fecha_caducidad, coste, lugar_compra):
        alimento = {
            "tipo_comida": tipo_comida,
            "marca": marca,
            "cantidad": cantidad,
            "fecha_compra": datetime.strptime(fecha_compra, "%Y-%m-%d"),
            "fecha_caducidad": datetime.strptime(fecha_caducidad, "%Y-%m-%d"),
            "coste": coste,
            "lugar_compra": lugar_compra
        }
    def guardar_csv(self, archivo):
        with open(archivo, mode='w', newline='') as file:
            campos = ["tipo_comida", "marca", "cantidad", "fecha_compra", "fecha_caducidad", "coste",
                          "lugar_compra"]
            writer = csv.DictWriter(file, fieldnames=campos)
            writer.writeheader()
            for comida in self.historial:
                writer.writerow({
                        "tipo_comida": comida["tipo_comida"],
                        "marca": comida["marca"],
                        "cantidad": comida["cantidad"],
                        "fecha_compra": comida["fecha_compra"].strftime("%Y-%m-%d"),
                        "fecha_caducidad": comida["fecha_caducidad"].strftime("%Y-%m-%d"),
                        "coste": comida["coste"],
                        "lugar_compra": comida["lugar_compra"]
                    })

    def cargar_csv(self, archivo):
        try:
            with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.añadir(
                            row["tipo_comida"],
                            row["marca"],
                            int(row["cantidad"]),
                            row["fecha_compra"],
                            row["fecha_caducidad"],
                            float(row["coste"]),
                            row["lugar_compra"]
                        )
        except FileNotFoundError:
            print(f"Archivo {archivo} no encontrado. Empezando con historial vacío.")

        # Sobrecarga de operadores
    def __len__(self):
        return len(self.historial)

    def __getitem__(self, index):
         return self.historial[index]

    def __add__(self, otro):
        nuevo = Alimentacion()
        nuevo.historial = self.historial + otro.historial
        return nuevo

    def __iadd__(self, otro):
        self.historial += otro.historial
        return self







