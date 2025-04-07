from animales import Animal

class Pez(Animal):
    """
    Clase Pez, que hereda todos los métodos y atributos de su superclase animal.
    """

    def __init__(self, id_mascota, nombre, fecha_nacimiento, raza, sexo, n_identificacion,
                 nombre_duenyo, apellido_duenyo, telefono_duenyo, email_duenyo, dni_duenyo, chip_registro):
        """
        Constructor de la clase Pez.
        Se fija 'Pez' como especie y llama al constructor de Animal.
        """
        especie = "Pez"
        super().__init__(id_mascota, nombre, fecha_nacimiento, especie, raza, sexo, n_identificacion,
                         nombre_duenyo, apellido_duenyo, telefono_duenyo, email_duenyo, dni_duenyo, chip_registro)


