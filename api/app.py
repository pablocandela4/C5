"""
api.py  ·  API RESTful Clínica Veterinaria

Ahora la información se guarda en la base de datos configurable
mediante la factoría `database.db` (SQLite local o MySQL en PythonAnywhere),
en lugar de mantenerse sólo en memoria.
"""

from flask import Flask, request, jsonify
from database import db

# (Opcional) si quieres seguir usando las clases para validar o procesar:
from animales.animal import Perro, Gato, Ave, Pez

app = Flask(__name__)


# ---------------------------------------------------------------------------
# RUTAS BÁSICAS
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    """GET / → Mensaje de bienvenida."""
    return "🐾 Bienvenido a la API de la Clínica Veterinaria"


# ---------------------------------------------------------------------------
# CRUD ANIMALES
# ---------------------------------------------------------------------------

@app.route("/animales", methods=["GET"])
def listar_animales():
    """
    GET /animales
    Devuelve un listado JSON con los animales almacenados en la BD.
    """
    return jsonify(db.get_animales()), 200


@app.route("/animales", methods=["POST"])
def crear_animal():
    """
    POST /animales
    Crea un nuevo animal. Ejemplo de cuerpo JSON:

    {
      "tipo": "perro",
      "chip": "1234",
      "nombre": "Fido",
      "edad": 4,
      "raza": "Labrador"
    }
    Campos mínimos: tipo, nombre
    """
    data = request.get_json(force=True)
    if not data:
        return {"error": "No se recibió JSON"}, 400

    tipo = data.get("tipo", "").lower()
    nombre = data.get("nombre")
    if not nombre or not tipo:
        return {"error": "Campos 'tipo' y 'nombre' son obligatorios"}, 400

    # --- (opcional) validación rápida usando las clases ya definidas ---
    try:
        match tipo:
            case "perro":
                _ = Perro(data.get("chip"), nombre, data.get("edad", 0), data.get("raza", ""))
            case "gato":
                _ = Gato(data.get("chip"), nombre, data.get("edad", 0), data.get("raza", ""))
            case "ave":
                _ = Ave(nombre, data.get("edad", 0))
            case "pez":
                _ = Pez(nombre, data.get("edad", 0))
            case _:
                return {"error": f"Tipo de animal '{tipo}' no reconocido"}, 400
    except Exception as e:
        return {"error": str(e)}, 400
    # ------------------------------------------------------------------

    # Insertamos en BD
    animal_id = db.insert_animal(
        {
            "tipo": tipo,
            "nombre": nombre,
            "edad": data.get("edad"),
            "chip": data.get("chip"),
            "raza": data.get("raza"),
        }
    )
    return {"mensaje": "Animal creado", "id": animal_id}, 200


@app.route("/animales/<int:animal_id>", methods=["PUT"])
def actualizar_animal(animal_id: int):
    """
    PUT /animales/<id>
    Cuerpo JSON con los campos a modificar (nombre, edad, raza, chip…).
    """
    cambios = request.get_json(force=True) or {}
    if not cambios:
        return {"error": "JSON vacío"}, 400

    db.update_animal(animal_id, cambios)
    return {"mensaje": "Animal actualizado"}, 200


@app.route("/animales/<int:animal_id>", methods=["DELETE"])
def borrar_animal(animal_id: int):
    """DELETE /animales/<id> → elimina registro."""
    db.delete_animal(animal_id)
    return {"mensaje": "Animal eliminado"}, 200


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Usa SQLite salvo que exportes DB_BACKEND=mysql
    app.run(debug=True, port=5000)
