"""
api.py

API RESTful con Flask para gestionar animales (Perro, Gato, Ave, Pez).
Lee y escribe datos en memoria (lista 'animales_registrados'), sin persistencia.

Autor: [Tu Nombre]
Fecha: [Fecha Actual]
"""

from flask import Flask, request, jsonify

from animales.animal import Perro, Gato, Ave, Pez

app = Flask(__name__)

# Lista global en memoria (reiniciable)
animales_registrados = []

@app.route("/")
def home():
    """
    GET /
    Muestra un mensaje de bienvenida de la API.
    """
    return "Bienvenido a la API de la Clínica Veterinaria"

@app.route("/animales", methods=["GET"])
def listar_animales():
    """
    GET /animales
    Devuelve un listado JSON con los animales en 'animales_registrados'.
    """
    # Convertimos cada animal en un diccionario con datos básicos
    resultado = []
    for a in animales_registrados:
        info = {
            "tipo": a.__class__.__name__,
            "chip": a.chip,
            "nombre": a.nombre,
            "especie": a.especie,
            "edad": a.edad
            
        }
        resultado.append(info)

    return jsonify(resultado), 200

@app.route("/animales", methods=["POST"])
def crear_animal():
    """
    POST /animales
    Crea un animal recibiendo JSON con al menos:
        - tipo: 'perro', 'gato', 'ave', 'pez'
        - nombre
        - edad
        - chip, raza (para perro/gato)
    
    Ejemplo de body JSON:
    {
      "tipo": "perro",
      "chip": "1234",
      "nombre": "Fido",
      "edad": 4,
      "raza": "Labrador"
    }
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se recibió JSON"}), 400

    tipo = data.get("tipo", "").lower()
    nombre = data.get("nombre", "SinNombre")
    edad = data.get("edad", 0)
    chip = data.get("chip", "")
    raza = data.get("raza", "Genérico")

    if tipo == "perro":
        nuevo = Perro(chip, nombre, edad, raza)
    elif tipo == "gato":
        nuevo = Gato(chip, nombre, edad, raza)
    elif tipo == "ave":
        # Ave no usa chip ni raza en tu código
        nuevo = Ave(nombre, edad)
    elif tipo == "pez":
        # Pez tampoco
        nuevo = Pez(nombre, edad)
    else:
        return jsonify({"error": f"Tipo de animal '{tipo}' no reconocido"}), 400

    animales_registrados.append(nuevo)
    return jsonify({"mensaje": f"Se registró el animal '{nombre}' de tipo '{tipo}' con éxito."}), 200



if __name__ == "__main__":
    
    app.run(debug=True)
