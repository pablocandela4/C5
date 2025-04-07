
from animales import Animal

class Perro(Animal):
    """
    Clase Perro, hereda todos los atributos y métodos de su superclase animal, no precisa de métodos específicos ya que nada se sobreecribe.
    """

    def __init__(self, id_mascota, nombre, fecha_nacimiento, raza, sexo, n_identificacion,
                 nombre_duenyo, apellido_duenyo, telefono_duenyo, email_duenyo, dni_duenyo, chip_registro):
        """
        Constructor de la clase Perro.
        Se fija 'Perro' como especie y llama al constructor de Animal.
        """
        especie = "Perro"
        super().__init__(id_mascota, nombre, fecha_nacimiento, especie, raza, sexo, n_identificacion,
                         nombre_duenyo, apellido_duenyo, telefono_duenyo, email_duenyo, dni_duenyo, chip_registro)