"""
api.py  ·  API RESTful Clínica Veterinaria

Ahora la información se guarda en la base de datos configurable
mediante la factoría `database.db` (SQLite local o MySQL en PythonAnywhere),
en lugar de mantenerse sólo en memoria.
"""

from flask import Flask, request, jsonify
from database import db

app = Flask(__name__)


@app.route("/")
def home():
    """GET / → Mensaje de bienvenida."""
    return "Bienvenida a la Clínica Veterinaria"



@app.route("/animales", methods=["GET"])
def listar_animales():
    """
    Devuelve un listado JSON con los animales almacenados en la BD.

    Returns
    -------
    json : list
        Listado de animales en formato JSON.
    int
        Código de estado HTTP 200 (OK).
    """
    return jsonify(db.listar_animales()), 200


@app.route("/animales", methods=["POST"])
def crear_animal():
    """
    Crea un nuevo animal

    Ejemplo de cuerpo JSON:
    {
      "tipo": "perro",
      "chip": "1234",
      "nombre": "Fido",
      "edad": 4,
    }

    Campos mínimos: tipo, nombre

    Returns
    -------
    json : dict
        Mensaje de éxito e ID del animal creado, o mensaje de error.
    int
        Código de estado HTTP 200 (OK) o 400 (Bad Request).
    """
    data = request.get_json(force=True)
    if not data:
        return {"error": "No se recibió JSON"}, 400

    chip = data.get("chip", "")
    nombre = data.get("nombre")
    edad = data.get("edad")
    raza = data.get("raza")
    especie = data.get("especie")
    if not nombre or not especie:
        return {"error": "Campos 'especie' y 'nombre' son obligatorios"}, 400


    if especie.lower() not in ["perro", "gato", "ave", "pez"]:
        return {"error": f"Tipo de animal '{especie}' no reconocido"}, 400



    # Inserta un animal en la base de datos dados unos valores
    animal_id = db.insert_animal(
        {
            "especie": especie,
            "nombre": nombre,
            "edad": edad,
            "chip": chip,
            "raza": raza,
        }
    )
    return {"mensaje": "Animal creado", "id": animal_id}, 200


@app.route("/animales/<int:animal_id>", methods=["PUT"])
def actualizar_animal(animal_id: int):
    """
    Actualiza un animal existente.

    Parameters
    ----------
    animal_id : int
        ID del animal a actualizar.

    Cuerpo JSON con los campos a modificar (nombre, edad, raza, chip…).

    Returns
    -------
    json : dict
        Mensaje de éxito o mensaje de error.
    int
        Código de estado HTTP 200 (OK) o 400 (Bad Request).
    """
    cambios = request.get_json(force=True) or {}
    if not cambios:
        return {"error": "JSON vacío"}, 400

    db.update_animal(animal_id, cambios)
    return {"mensaje": "Animal actualizado"}, 200


@app.route("/animales/<int:animal_id>", methods=["DELETE"])
def borrar_animal(animal_id: int):
    """
    Elimina un animal.

    Parameters
    ----------
    animal_id : int
        ID del animal a eliminar.

    Returns
    -------
    json : dict
        Mensaje de éxito.
    int
        Código de estado HTTP 200 (OK).
    """
    db.delete_animal(animal_id)
    return {"mensaje": "Animal eliminado"}, 200


# PERSONA DUEÑO

@app.route("/dueno", methods=["GET"])
def listar_dueno():
    """
    Devuelve un listado JSON con todos los dueños.

    Returns
    -------
    json : list
        Listado de dueños en formato JSON.
    int
        Código de estado HTTP 200 (OK).
    """
    return jsonify(db.listar_duenos()), 200
@app.route("/dueno", methods=["POST"])
def crear_dueno():
    """
    Crea un nuevo dueño.

    Cuerpo JSON con los datos del dueño (nombre, nif, dirección, teléfono).
    Campos mínimos: nombre, nif

    Returns
    -------
    json : dict
        Mensaje de éxito e ID del dueño creado, o mensaje de error.
    int
        Código de estado HTTP 200 (OK) o 400 (Bad Request).
    """
    data = request.get_json(force=True)
    if not data:
        return {"error": "No se recibió JSON"}, 400

    nombre = data.get("nombre")
    nif = data.get("nif")
    direccion = data.get("direccion")
    telefono = data.get("telefono")
    if not nombre or not nif:
        return {"error": "Campos 'nif' y 'nombre' son obligatorios"}, 400


    dueno_id = db.insert_dueno(
        {
            "nombre": nombre,
            "nif": nif,
            "direccion": direccion,
            "telefono": telefono,
        }
    )
    return {"mensaje": "Dueño", "id": dueno_id}, 200


@app.route("/dueno/<int:dueno_id>", methods=["PUT"])
def actualizar_dueno(dueno_id: int):
    """
    Actualiza la información de un dueño.

    Parameters
    ----------
    dueno_id : int
        ID del dueño a actualizar.

    Cuerpo JSON con los campos a modificar (nombre, nif, dirección, teléfono).

    Returns
    -------
    json : dict
        Mensaje de éxito o mensaje de error.
    int
        Código de estado HTTP 200 (OK) o 400 (Bad Request).
    """
    cambios = request.get_json(force=True) or {}
    if not cambios:
        return {"error": "JSON vacío"}, 400

    db.update_dueno(dueno_id, cambios)
    return {"mensaje": " Dueño actualizado"}, 200


@app.route("/dueno/<int:dueno_id>", methods=["DELETE"])
def borrar_dueno(dueno_id: int):
    """
    Elimina un dueño.

    Parameters
    ----------
    dueno_id : int
        ID del dueño a eliminar.

    Returns
    -------
    json : dict
        Mensaje de éxito.
    int
        Código de estado HTTP 200 (OK).
    """
    db.delete_dueno(dueno_id)
    return {"mensaje": "Dueño eliminado"}, 200
@app.route("/veterinario", methods=["GET"])

# PERSONA VETERINARIO
def listar_veterinario():
    """
    Devuelve un listado JSON con todos los veterinarios.

    Returns
    -------
    json : list
        Listado de veterinarios en formato JSON.
    int
        Código de estado HTTP 200 (OK).
    """
    return jsonify(db.listar_veterinarios()), 200
@app.route("/veterinario", methods=["POST"])
def crear_veterinario():
    """
    Crea un nuevo veterinario.

    Cuerpo JSON con los datos del veterinario (nombre, nif, dirección, teléfono, colegiado_id).
    Campos mínimos: nombre, colegiado_id

    Returns
    -------
    json : dict
        Mensaje de éxito e ID del veterinario creado, o mensaje de error.
    int
        Código de estado HTTP 200 (OK) o 400 (Bad Request).
    """
    data = request.get_json(force=True)
    if not data:
        return {"error": "No se recibió JSON"}, 400

    nombre = data.get("nombre")
    nif = data.get("nif")
    direccion = data.get("direccion")
    telefono = data.get("telefono")
    colegiado_id = data.get("colegiado_id")
    if not nombre or not colegiado_id:
        return {"error": "Campos 'colegiado_id' y 'nombre' son obligatorios"}, 400


    veterinario_id = db.insert_veterinario(
        {
            "nombre": nombre,
            "nif": nif,
            "direccion": direccion,
            "colegiado_id": colegiado_id,
            "telefono": telefono,
        }
    )
    return {"mensaje": "Veterinario creado", "id": veterinario_id}, 200


@app.route("/veterinario/<int:veterinario_id>", methods=["PUT"])
def actualizar_veterinario(veterinario_id: int):
    """
    Actualiza la información de un veterinario.

    Parameters
    ----------
    veterinario_id : int
        ID del veterinario a actualizar.

    Cuerpo JSON con los campos a modificar (nombre, nif, dirección, teléfono, colegiado_id).

    Returns
    -------
    json : dict
        Mensaje de éxito o mensaje de error.
    int
        Código de estado HTTP 200 (OK) o 400 (Bad Request).
    """
    cambios = request.get_json(force=True) or {}
    if not cambios:
        return {"error": "JSON vacío"}, 400

    db.update_veterinario(veterinario_id, cambios)
    return {"mensaje": " Veterinario actualizado"}, 200


@app.route("/veterinario/<int:veterinario_id>", methods=["DELETE"])
def borrar_veterinario(veterinario_id: int):
    """
    Elimina un veterinario.

    Parameters
    ----------
    veterinario_id : int
        ID del veterinario a eliminar.

    Returns
    -------
    json : dict
        Mensaje de éxito.
    int
        Código de estado HTTP 200 (OK).
    """
    db.delete_veterinario(veterinario_id)
    return {"mensaje": "Veterinario eliminado"}, 200

@app.route("/alimento", methods=["GET"])
def listar_alimentos():
    """Devuelve un listado JSON con todos los alimentos."""
    return jsonify(db.listar_alimentos()), 200

@app.route("/alimento", methods=["POST"])
def crear_alimento():
    """Crea un nuevo alimento."""
    data = request.get_json(force=True)
    if not data:
        return {"error": "No se recibió JSON"}, 400

    tipo_animal = data.get("tipo_animal")
    alimento = data.get("alimento")
    cantidad = data.get("cantidad")
    fecha_caducidad = data.get("fecha_caducidad")
    coste = data.get("coste")

    if not tipo_animal or not alimento or cantidad is None:
        return {"error": "Campos 'tipo_animal', 'alimento' y 'cantidad' son obligatorios"}, 400

    alimento_id = db.insert_alimento(
        {
            "tipo_animal": tipo_animal,
            "alimento": alimento,
            "cantidad": cantidad,
            "fecha_caducidad": fecha_caducidad,
            "coste": coste,
        }
    )
    return {"mensaje": "Alimento creado", "id": alimento_id}, 200

@app.route("/alimento/<int:alimento_id>", methods=["PUT"])
def actualizar_alimento(alimento_id: int):
    """Actualiza la información de un alimento."""
    cambios = request.get_json(force=True) or {}
    if not cambios:
        return {"error": "JSON vacío"}, 400
    db.update_alimento(alimento_id, cambios)
    return {"mensaje": "Alimento actualizado"}, 200

@app.route("/alimento/<int:alimento_id>", methods=["DELETE"])
def borrar_alimento(alimento_id: int):
    """Elimina un alimento."""
    db.delete_alimento(alimento_id)
    return {"mensaje": "Alimento eliminado"}, 200

if __name__ == "__main__":

    app.run(debug=True, port=5000)

