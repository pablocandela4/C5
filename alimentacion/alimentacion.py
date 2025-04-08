import csv
from datetime import datetime

class Alimentacion:
    def __init__(self, alimento, tipo_comida, cantidad, fecha_caducidad, coste):
        self.alimento = alimento
        self.tipo_comida = tipo_comida
        self.cantidad = cantidad  # en gramos
        self.fecha_caducidad = datetime.strptime(fecha_caducidad, "%Y-%m-%d")
        self.coste = float(coste)

    def __str__(self):
        return (
            f"{self.tipo_comida} | {self.cantidad}g | "
            f"Datos: caduca en {self.fecha_caducidad.date()} y tiene un coste de {self.coste}€ | "
        )


class HistorialAlimentacion(Alimentacion):
    def __init__(self, alimento, tipo_comida, cantidad, fecha_caducidad, coste):
        super().__init__(alimento, tipo_comida, cantidad, fecha_caducidad, coste)
        self.alimentos =[]

    def __str__(self):
        if not self.alimentos:
            return "  - Sin alimentos registrados"
        return "\n".join(f"  - {v}" for v in self.alimentos)

    def agregar_alimento(self, alimento, auto_guardar=True, archivo='alimetacion.csv'):
        self.alimentos.append(alimento)
        if auto_guardar:
            self.guardar_csv(archivo)

    def guardar_csv(self, archivo='alimentacion.csv'):
        with open(archivo, mode='w', newline='') as file:
            campos = ["tipo_comida", "marca", "cantidad", "fecha_caducidad", "coste"]
            writer = csv.DictWriter(file, fieldnames=campos)
            writer.writeheader()
            for a in self.alimentos:
                writer.writerow({
                    'alimento': a.alimento,
                    "tipo_comida": a.tipo_comida,
                    "cantidad": a.cantidad,
                    "fecha_caducidad": a.fecha_caducidad.strftime("%Y-%m-%d"),
                    "coste": f"{a.coste:.2f}",
                })

    def cargar_csv(self, archivo):
        try:
            with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    alimento = Alimentacion(
                        row['alimento'],
                        row["tipo_comida"],
                        int(row["cantidad"]),
                        row["fecha_caducidad"],
                        float(row["coste"])
                    )
                    self.agregar_alimento(alimento)
        except FileNotFoundError:
            print(f"Archivo {archivo} no encontrado.")

    # Sobrecarga de operadores
    def __len__(self):
        return len(self.alimentos)

    def __getitem__(self, index):
         return self.alimentos[index]

    def __add__(self, otro):
        nuevo = HistorialAlimentacion()
        nuevo.alimentos = self.alimentos + otro.alimentos
        return nuevo

    def __iadd__(self, otro):
        self.alimentos += otro.alimentos
        return self







