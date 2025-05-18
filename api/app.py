
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
    return "🐾 Bienvenido a la API de la Clínica Veterinaria"


# ------------------- CRUD ANIMALES -------------------
@app.route("/animales", methods=["GET"])
def listar_animales():
    return jsonify(db.get_animales()), 200


@app.route("/animales", methods=["POST"])
def crear_animal():
    data = request.get_json(force=True)
    if not data:
        return {"error": "No se recibió JSON"}, 400

    tipo = data.get("tipo", "").lower()
    nombre = data.get("nombre")
    edad = data.get("edad")
    chip = data.get("chip")
    raza = data.get("raza")

    if not tipo or not nombre:
        return {"error": "Campos 'tipo' y 'nombre' son obligatorios"}, 400

    try:
        match tipo:
            case "perro":
                _ = Perro(chip, nombre, edad or 0, raza or "")
            case "gato":
                _ = Gato(chip, nombre, edad or 0, raza or "")
            case "ave":
                _ = Ave(nombre, edad or 0)
            case "pez":
                _ = Pez(nombre, edad or 0)
            case _:
                return {"error": f"Tipo de animal '{tipo}' no reconocido"}, 400
    except Exception as e:
        return {"error": str(e)}, 400

    animal_id = db.insert_animal({
        "tipo": tipo,
        "nombre": nombre,
        "edad": edad,
        "chip": chip,
        "raza": raza,
    })
    return {"mensaje": "Animal creado", "id": animal_id}, 200


@app.route("/animales/<int:animal_id>", methods=["PUT"])
def actualizar_animal(animal_id: int):
    cambios = request.get_json(force=True) or {}
    if not cambios:
        return {"error": "JSON vacío"}, 400

    db.update_animal(animal_id, cambios)
    return {"mensaje": "Animal actualizado"}, 200


@app.route("/animales/<int:animal_id>", methods=["DELETE"])
def borrar_animal(animal_id: int):
    db.delete_animal(animal_id)
    return {"mensaje": "Animal eliminado"}, 200


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


# ------------------- RUN -------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
