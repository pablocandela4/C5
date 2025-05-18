"""
db_base.py
Clase base para la gestión de la base de datos de la clínica veterinaria.
Define la interfaz que deben implementar los gestores de bases de datos específicos (SQLite, MySQL, etc.).
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class DBManager(ABC):
    """
    Interfaz para la gestión de la base de datos de la clínica veterinaria.
    Define operaciones CRUD para animales, dueños y veterinarios.
    """

    @abstractmethod
    def insertar_animal(self, datos: Dict[str, Any]) -> int:
        """
        Inserta un nuevo animal en la base de datos.

        Parameters
        ----------
        datos : Dict[str, Any]
            Diccionario con los datos del animal a insertar.
            Debe contener las claves: 'especie', 'nombre'.
            Puede contener opcionalmente: 'edad', 'chip', 'raza'.

        Returns
        -------
        int
            El ID del animal insertado.

        Raises
        ------
        Exception
            Si ocurre un error durante la inserción.
        """
        pass

    @abstractmethod
    def obtener_animales(self) -> List[Dict[str, Any]]:
        """
        Obtiene todos los animales de la base de datos. List.

        Returns
        -------
        List[Dict[str, Any]]
            Una lista de diccionarios, donde cada diccionario representa un animal.
            Las claves de cada diccionario son: 'id', 'especie', 'nombre', 'edad', 'chip', 'raza'.
            Si no hay animales, devuelve una lista vacía.

        Raises
        ------
        Exception
            Si ocurre un error durante la consulta.
        """
        pass

    @abstractmethod
    def obtener_animal(self, animal_id: int) -> Optional[Dict[str, Any]]:
        """
        Obtiene un animal por su ID.
        Parameters
        ----------
        animal_id: int
            el id del animal

        Returns
        -------
        Optional[Dict[str, Any]]:
            Un diccionario representando al animal si se encuentra, None si no.
        """
        pass

    @abstractmethod
    def actualizar_animal(self, animal_id: int, datos: Dict[str, Any]) -> None:
        """
        Actualiza la información de un animal existente.

        Parameters
        ----------
        animal_id : int
            ID del animal a actualizar.
        datos : Dict[str, Any]
            Diccionario con los datos a actualizar.  Puede contener cualquier
            combinación de las claves: 'especie', 'nombre', 'edad', 'chip', 'raza'.

        Raises
        ------
        Exception
            Si el animal no existe o si ocurre un error durante la actualización.
        """
        pass

    @abstractmethod
    def eliminar_animal(self, animal_id: int) -> None:
        """
        Elimina un animal de la base de datos.

        Parameters
        ----------
        animal_id : int
            ID del animal a eliminar.

        Raises
        ------
        Exception
            Si el animal no existe o si ocurre un error durante la eliminación.
        """
        pass

    @abstractmethod
    def insertar_dueno(self, datos: Dict[str, Any]) -> int:
        """
        Inserta un nuevo dueño en la base de datos.

        Parameters
        ----------
        datos : Dict[str, Any]
            Diccionario con los datos del dueño a insertar.
            Debe contener las claves: 'nombre', 'nif'.
            Puede contener opcionalmente: 'direccion', 'telefono'.

        Returns
        -------
        int
            El ID del dueño insertado.

        Raises
        ------
        Exception
            Si ocurre un error durante la inserción.
        """
        pass

    @abstractmethod
    def obtener_duenos(self) -> List[Dict[str, Any]]:
        """
        Obtiene todos los dueños de la base de datos.

        Returns
        -------
        List[Dict[str, Any]]
            Una lista de diccionarios, donde cada diccionario representa un dueño.
            Las claves de cada diccionario son: 'id', 'nombre', 'nif', 'direccion', 'telefono'.
            Si no hay dueños, devuelve una lista vacía.

        Raises
        ------
        Exception
            Si ocurre un error durante la consulta.
        """
        pass

    @abstractmethod
    def obtener_dueno(self, dueno_id: int) -> Optional[Dict[str, Any]]:
        """
        Obtiene un dueño por su ID.
        Parameters
        ----------
        dueno_id: int
            el id del dueño

        Returns
        -------
        Optional[Dict[str, Any]]:
            Un diccionario representando al dueño si se encuentra, None si no.
        """
        pass

    @abstractmethod
    def actualizar_dueno(self, dueno_id: int, datos: Dict[str, Any]) -> None:
        """
        Actualiza la información de un dueño existente.

        Parameters
        ----------
        dueno_id : int
            ID del dueño a actualizar.
        datos : Dict[str, Any]
            Diccionario con los datos a actualizar.  Puede contener cualquier
            combinación de las claves: 'nombre', 'nif', 'direccion', 'telefono'.

        Raises
        ------
        Exception
            Si el dueño no existe o si ocurre un error durante la actualización.
        """
        pass

    @abstractmethod
    def eliminar_dueno(self, dueno_id: int) -> None:
        """
        Elimina un dueño de la base de datos.

        Parameters
        ----------
        dueno_id : int
            ID del dueño a eliminar.

        Raises
        ------
        Exception
            Si el dueño no existe o si ocurre un error durante la eliminación.
        """
        pass

    @abstractmethod
    def insertar_veterinario(self, datos: Dict[str, Any]) -> int:
        """
        Inserta un nuevo veterinario en la base de datos.

        Parameters
        ----------
        datos : Dict[str, Any]
            Diccionario con los datos del veterinario a insertar.
            Debe contener las claves: 'nombre', 'colegiado_id'.
            Puede contener opcionalmente: 'nif', 'direccion', 'telefono'.

        Returns
        -------
        int
            El ID del veterinario insertado.

        Raises
        ------
        Exception
            Si ocurre un error durante la inserción.
        """
        pass

    @abstractmethod
    def obtener_veterinarios(self) -> List[Dict[str, Any]]:
        """
        Obtiene todos los veterinarios de la base de datos.

        Returns
        -------
        List[Dict[str, Any]]
            Una lista de diccionarios, donde cada diccionario representa un veterinario.
            Las claves del diccionario son: 'id', 'nombre', 'nif', 'direccion', 'telefono', 'colegiado_id'.
            Si no hay veterinarios, devuelve una lista vacía.

        Raises
        ------
        Exception
            Si ocurre un error durante la consulta.
        """
        pass

    @abstractmethod
    def obtener_veterinario(self, colegiado_id: int) -> Optional[Dict[str, Any]]:
        """
        Obtiene un veterinario por su colegiado_id.
        Parameters
        ----------
        colegiado_id: int
            el colegiado_id del veterinario

        Returns
        -------
        Optional[Dict[str, Any]]:
            Un diccionario representando al veterinario si se encuentra, None si no.
        """
        pass

    @abstractmethod
    def actualizar_veterinario(self, colegiado_id: int, datos: Dict[str, Any]) -> None:
        """
        Actualiza la información de un veterinario existente.

        Parameters
        ----------
        colegiado_id : int
            ID del veterinario a actualizar.
        datos : Dict[str, Any]
            Diccionario con los datos a actualizar.  Puede contener cualquier
            combinación de las claves: 'nombre', 'nif', 'direccion', 'telefono', 'colegiado_id'.

        Raises
        ------
        Exception
            Si el veterinario no existe o si ocurre un error durante la actualización.
        """
        pass

    @abstractmethod
    def eliminar_veterinario(self, colegiado_id: int) -> None:
        """
        Elimina un veterinario de la base de datos.

        Parameters
        ----------
        colegiado_id : int
            ID del veterinario a eliminar.

        Raises
        ------
        Exception
            Si el veterinario no existe o si ocurre un error durante la eliminación.
        """
        pass
