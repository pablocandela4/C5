import csv
from datetime import datetime
from animales import Animal


class Historial:
    def __init__(self, nombre):
        self.nombre = nombre
    def mostrar_historial_completo(nombre_mascota, alimentacion_obj):
        print(f"\n📦 HISTORIAL DE ALIMENTACIÓN DE {nombre_mascota.upper()}")
        print("-" * 60)
        if len(alimentacion_obj) == 0:
            print("Sin registros.")
        else:
            alimentacion_obj.mostrar()
