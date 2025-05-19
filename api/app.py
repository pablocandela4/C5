"""
app.py · API RESTful Clínica Veterinaria

• CRUD animales
• CRUD cuidados
• CRUD dueños y veterinarios
"""

from __future__ import annotations
from datetime import datetime
from typing import Any, Dict

from flask import Flask, jsonify, request
from database import db

from animales.animal import Perro, Gato, Ave, Pez
from cuidados.cuidado_base import CuidadoProgramado
from cuidados.cuidado_perro import CuidadoPerro
from cuidados.cuidado_gato import CuidadoGato
from cuidados.cuidado_ave import CuidadoAve
from cuidados.cuidado_pez import CuidadoPez

app = Flask(__name__)


def _validar_fecha(fecha_txt: str) -> str:
    try:
        datetime.strptime(fecha_txt, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("La fecha debe estar en formato YYYY-MM-DD") from exc
    return fecha_txt


@app.route("/")
def home():
    return " Bienvenido a la API de la Clínica Veterinaria"


# ------------------- CRUD ANIMALES -------------------

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


# ------------------- CRUD CUIDADOS -------------------
@app.route("/cuidados", methods=["GET"])
def listar_cuidados():
    return jsonify(db.get_cuidados()), 200


@app.route("/animales/<int:animal_id>/cuidados", methods=["GET"])
def listar_cuidados_animal(animal_id: int):
    return jsonify(db.get_cuidados(animal_id)), 200


@app.route("/cuidados", methods=["POST"])
def crear_cuidado():
    data: Dict[str, Any] = request.get_json(force=True) or {}
    try:
        animal_id = int(data["animal_id"])
        fecha = _validar_fecha(data["fecha"])
        tipo_cuidado = data["tipo"]
    except (KeyError, ValueError) as e:
        return {"error": f"Campos requeridos faltantes o inválidos: {e}"}, 400

    tipo_animal = next(
        (a["tipo"] for a in db.get_animales() if a["chip"] == animal_id), None
    )
    clase = {
        "perro": CuidadoPerro,
        "gato": CuidadoGato,
        "ave": CuidadoAve,
        "pez": CuidadoPez,
    }.get(tipo_animal, CuidadoProgramado)

    try:
        _ = clase(
            fecha=fecha,
            tipo_cuidado=tipo_cuidado,
            animal_id=animal_id,
            estado=data.get("estado", "pendiente"),
            notas=data.get("notas", ""),
        )
    except Exception as e:
        return {"error": str(e)}, 400

    cuidado_id = db.insert_cuidado({
        "animal_id": animal_id,
        "fecha": fecha,
        "tipo": tipo_cuidado,
        "estado": data.get("estado", "pendiente"),
        "notas": data.get("notas", ""),
    })
    return {"mensaje": "Cuidado creado", "id": cuidado_id}, 201


@app.route("/cuidados/<int:cuidado_id>", methods=["PUT"])
def actualizar_cuidado(cuidado_id: int):
    cambios = request.get_json(force=True) or {}
    if not cambios:
        return {"error": "JSON vacío"}, 400

    if "fecha" in cambios:
        try:
            cambios["fecha"] = _validar_fecha(cambios["fecha"])
        except ValueError as e:
            return {"error": str(e)}, 400

    db.update_cuidado(cuidado_id, cambios)
    return {"mensaje": "Cuidado actualizado"}, 200


@app.route("/cuidados/<int:cuidado_id>", methods=["DELETE"])
def borrar_cuidado(cuidado_id: int):
    db.delete_cuidado(cuidado_id)
    return {"mensaje": "Cuidado eliminado"}, 200


# ------------------- CRUD ALIMENTO -------------------
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

    alimento_id = db.insert_alimento({
        "tipo_animal": tipo_animal,
        "alimento": alimento,
        "cantidad": cantidad,
        "fecha_caducidad": fecha_caducidad,
        "coste": coste,
    })
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


# ------------------- CRUD VACUNAS -------------------
@app.route("/vacuna", methods=["GET"])
def listar_vacunas():
    """Devuelve un listado JSON con todas las vacunas."""
    return jsonify(db.listar_vacunas()), 200


@app.route("/vacuna", methods=["POST"])
def crear_vacuna():
    """Crea una nueva vacuna."""
    data = request.get_json(force=True)
    if not data:
        return {"error": "No se recibió JSON"}, 400

    nombre = data.get("nombre")
    fecha = data.get("fecha")

    if not nombre or not fecha:
        return {"error": "Campos 'nombre' y 'fecha' son obligatorios"}, 400

    vacuna_id = db.insert_vacuna({
        "nombre": nombre,
        "fecha": fecha,
    })
    return {"mensaje": "Vacuna creada", "id": vacuna_id}, 200


@app.route("/vacuna/<int:vacuna_id>", methods=["PUT"])
def actualizar_vacuna(vacuna_id: int):
    """Actualiza la información de una vacuna."""
    cambios = request.get_json(force=True) or {}
    if not cambios:
        return {"error": "JSON vacío"}, 400
    db.update_vacuna(vacuna_id, cambios)
    return {"mensaje": "Vacuna actualizada"}, 200


@app.route("/vacuna/<int:vacuna_id>", methods=["DELETE"])
def borrar_vacuna(vacuna_id: int):
    """Elimina una vacuna."""
    db.delete_vacuna(vacuna_id)
    return {"mensaje": "Vacuna eliminada"}, 200


# ------------------- CRUD TRATAMIENTO -------------------
@app.route("/tratamiento", methods=["GET"])
def listar_tratamientos():
    """Devuelve un listado JSON con todos los tratamientos."""
    return jsonify(db.listar_tratamientos()), 200


@app.route("/tratamiento", methods=["POST"])
def crear_tratamiento():
    """Crea un nuevo tratamiento."""
    data = request.get_json(force=True)
    if not data:
        return {"error": "No se recibió JSON"}, 400

    nombre = data.get("nombre")
    fecha_inicio = data.get("fecha_inicio")
    fecha_fin = data.get("fecha_fin")
    coste = data.get("coste")

    if not nombre or not fecha_inicio or not fecha_fin or coste is None:
        return {"error": "Todos los campos son obligatorios"}, 400

    tratamiento_id = db.insert_tratamiento({
        "nombre": nombre,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "coste": coste,
    })
    return {"mensaje": "Tratamiento creado", "id": tratamiento_id}, 200


@app.route("/tratamiento/<int:tratamiento_id>", methods=["PUT"])
def actualizar_tratamiento(tratamiento_id: int):
    """Actualiza la información de un tratamiento."""
    cambios = request.get_json(force=True) or {}
    if not cambios:
        return {"error": "JSON vacío"}, 400
    db.update_tratamiento(tratamiento_id, cambios)
    return {"mensaje": "Tratamiento actualizado"}, 200


@app.route("/tratamiento/<int:tratamiento_id>", methods=["DELETE"])
def borrar_tratamiento(tratamiento_id: int):
    """Elimina un tratamiento."""
    db.delete_tratamiento(tratamiento_id)
    return {"mensaje": "Tratamiento eliminado"}, 200


# ------------------- CRUD CONSULTA -------------------
@app.route("/consulta", methods=["GET"])
def listar_consultas():
    """Devuelve un listado JSON con todas las consultas."""
    return jsonify(db.listar_consultas()), 200


@app.route("/consulta", methods=["POST"])
def crear_consulta():
    """Crea una nueva consulta."""
    data = request.get_json(force=True)
    if not data:
        return {"error": "No se recibió JSON"}, 400

    animal = data.get("animal")
    veterinario = data.get("veterinario")
    fecha = data.get("fecha")
    diagnostico = data.get("diagnostico")

    if not animal or not veterinario or not fecha or not diagnostico:
        return {"error": "Todos los campos son obligatorios"}, 400

    consulta_id = db.insert_consulta({
        "animal": animal,
        "veterinario": veterinario,
        "fecha": fecha,
        "diagnostico": diagnostico,
    })
    return {"mensaje": "Consulta creada", "id": consulta_id}, 200


@app.route("/consulta/<int:consulta_id>", methods=["PUT"])
def actualizar_consulta(consulta_id: int):
    """Actualiza la información de una consulta."""
    cambios = request.get_json(force=True) or {}
    if not cambios:
        return {"error": "JSON vacío"}, 400
    db.update_consulta(consulta_id, cambios)
    return {"mensaje": "Consulta actualizada"}, 200


@app.route("/consulta/<int:consulta_id>", methods=["DELETE"])
def borrar_consulta(consulta_id: int):
    """Elimina una consulta."""
    db.delete_consulta(consulta_id)
    return {"mensaje": "Consulta eliminada"}, 200


# ------------------- RUN -------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
