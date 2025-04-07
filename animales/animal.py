import csv
from abc import ABC
from datetime import datetime

class Animal(ABC):
    """
    Animal es la clase base para todas las mascotas, ya sean perro, pez, gato o ave.
    Aquí se guardarán todos los atributos de los dueños, los historiales de vacunas, alimentación, cuidados y compras.
    """

    def __init__(self, id_mascota, nombre, fecha_nacimiento, especie, raza, sexo, n_identificacion,
                 nombre_duenyo, apellido_duenyo, telefono_duenyo, email_duenyo, dni_duenyo, chip_registro):

        self.id_mascota = id_mascota
        self.nombre = nombre
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        self.especie = especie
        self.raza = raza
        self.sexo = sexo
        self.numero_identificacion = n_identificacion

        self.nombre_dueño = nombre_duenyo
        self.apellido_dueño = apellido_duenyo
        self.telefono_dueño = telefono_duenyo
        self.email_dueño = email_duenyo
        self.dni_dueño = dni_duenyo
        self.chip_registro = chip_registro

        self.vacunas = []
        self.alimentacion = []
        self.cuidados = []
        self.compras = []

    """
    Método mágico para imprimir animal 
    """

    def __str__(self):
        return f"{self.nombre} ({self.especie}, ID: {self.id_mascota})"

    """
    la función de registro mascota, únicamente nos devuelve la información asociada a las mismas
    """

    def registro_mascota(self):
        return {
            "ID": self.id_mascota,
            "Nombre": self.nombre,
            "Fecha nacimiento": self.fecha_nacimiento.strftime("%Y-%m-%d"),
            "Especie": self.especie,
            "Raza": self.raza,
            "Sexo": self.sexo,
            "ID Animal": self.n_identificacion,
            "Dueño": f"{self.nombre_duenyo} {self.apellido_duenyo}",
            "Teléfono": self.telefono_duenyo,
            "Email": self.email_duenyo,
            "DNI": self.dni_duenyo,
            "Chip": self.chip_registro
        }

    """
    Función para guardar en un csv con nombre animales los datos asociados al registro de las mascotas
    """

    def guardar_en_csv(self, archivo="animales.csv"):
        datos = self.registro_mascota()
        with open(archivo, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=datos.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(datos)

    """
    Carga los registros de mascotas desde un archivo CSV (devuelve una lista de diccionarios)
    """

    @staticmethod
    def cargar_mascotas_desde_csv(archivo="animales.csv"):

        mascotas = []
        try:
            with open(archivo, mode='r') as file:
                reader = csv.DictReader(file)
                for registro in reader:
                    mascotas.append(registro)
        except FileNotFoundError:
            print(f"No se encontró el archivo {archivo}.")
        return mascotas

    """
      VACUNAS,  tendremos como métodos agregar y mostrar. Están relacionadas con el historial médico de la mascota. Por ello se registra el número de la vacina, la fecha en la que se puso, el veterinario(n_colegiado)que se la puso y el coste
      """

    def agregar_vacuna(self, n_vacuna, fecha, n_colegiado, coste):

        self.vacunas.append({
            "n_vacuna": n_vacuna,
            "fecha": datetime.strptime(fecha, "%Y-%m-%d"),
            "n_colegiado": n_colegiado,
            "coste": coste
        })

    def mostrar_vacunas(self):
        """
        Muestra las vacunas registradas.
        """
        for vacuna in self.vacunas:
            print(
                f"- {vacuna['n_vacuna']} | Fecha: {vacuna['fecha']} | Colegiado: {vacuna['n_colegiado']} | Coste: {vacuna['coste']}€")

    """
      ALIMENTACION,  tenemos como métodos el agregar el tipo de comida, la marca, la cantidad, cuando se compró, la caducidad, el coste y mostrar esa alimentación
      """

    def agregar_alimento(self, tipo_comida, marca, cantidad, fecha_compra, fecha_caducidad, coste):

        self.alimentacion.append({
            "tipo_comida": tipo_comida,
            "marca": marca,
            "cantidad": cantidad,
            "fecha_compra": datetime.strptime(fecha_compra, "%Y-%m-%d"),
            "fecha_caducidad": datetime.strptime(fecha_caducidad, "%Y-%m-%d"),
            "coste": coste,

        })

    def mostrar_alimentacion(self):
        for registro in self.alimentacion:
            print(
                f"- {registro['tipo_comida']} ({registro['marca']}) | Cantidad: {registro['cantidad']}g | Compra: {registro['fecha_compra']} | Caduca: {registro['fecha_caducidad']} | {registro['coste']}€ en {registro['lugar_compra']}")

    """ 
    Funciones asociadas al cuidado de las mascotas
    """

    def agregar_cuidado(self, tipo, fecha, estado="pendiente", comentario="", id_profesional=None):
        """Agrega un cuidado o recordatorio al historial."""
        self.cuidados.append({
            "tipo": tipo,
            "fecha": datetime.strptime(fecha, "%Y-%m-%d"),
            "estado": estado,
            "comentario": comentario,
            "id_profesional": id_profesional
        })

    def mostrar_cuidados(self):
        """
        Muestra todos los cuidados registrados.
        """
        for cuidado in self.cuidados:
            print(
                f"- {cuidado['tipo']} | Fecha: {cuidado['fecha']} | Estado: {cuidado['estado']} | Comentario: {cuidado['comentario']} | Profesional: {cuidado['id_profesional']}")

    def marcar_cuidado_realizado(self, indice):
        """
        Marca un cuidado como realizado (según su posición en la lista).
        """
        if 0 <= indice < len(self.cuidados):
            self.cuidados[indice]['estado'] = "realizado"

    """
      Función de compra de mascota
      """

    def compra_mascota(self, id_vendedor, fecha_compra, coste):
        """Registra la compra de la mascota."""
        self.compras.append({
            "dni_dueño": self.dni_duenyo,
            "id_mascota": self.id_mascota,
            "id_vendedor": id_vendedor,
            "fecha_compra": datetime.strptime(fecha_compra, "%Y-%m-%d"),
            "coste": coste
        })

    def mostrar_historial_compra(self):
        """
        Muestra el historial de compra de la mascota. Y en el aparecen tanto los datos asociados al vendedor como a la fecha de compra o el coste. El identificativo del dueño será el dni
        """
        for compra in self.compras:
            print(
                f"Comprada por DNI {compra['dni_duenyo']} desde vendedor ID {compra['id_vendedor']} en {compra['fecha_compra']} por {compra['coste']}€")

    """ 
    Funcion historial, esta función recoge todos los datos asociados a nuestra tienda de mascotas en el que aparecen los datos del dueño,los cuidados, las vacunas, la alimentación y el historial de compra asociado
    """

    def historial(self):
        """Muestra toda la información acumulada de la mascota."""
        print(f"\n HISTORIAL: {self.nombre} ---")
        print("\n Datos del Dueño:")
        print(f"Nombre: {self.nombre_duenyo} {self.apellido_duenyo} | DNI: {self.dni_duenyo}")
        print("\n Cuidados:")
        self.mostrar_cuidados()
        print("\n Vacunas:")
        self.mostrar_vacunas()
        print("\n Alimentación:")
        self.mostrar_alimentacion()
        print("\n Historial de compra:")
        self.mostrar_historial_compra()
