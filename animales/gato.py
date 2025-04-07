from animales import Animal

class Gato(Animal):
    """
    Clase Gato, que hereda todos los métodos y los atributos de la superclase animal.
    """

    def __init__(self, id_mascota, nombre, fecha_nacimiento, raza, sexo, n_identificacion,
                 nombre_duenyo, apellido_duenyo, telefono_duenyo, email_duenyo, dni_duenyo, chip_registro):
        """
        Constructor de la clase Gato.
        Se fija 'Gato' como especie y llama al constructor de Animal.
        """
        especie = "Gato"
        super().__init__(id_mascota, nombre, fecha_nacimiento, especie, raza, sexo, n_identificacion,
                         nombre_duenyo, apellido_duenyo, telefono_duenyo, email_duenyo, dni_duenyo, chip_registro)

