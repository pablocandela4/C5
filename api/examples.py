"""
examples.py

Script de consola (CLI) para interactuar con la API RESTful definida en api.py.

Ofrece un menú con opciones:
    1. Ver animales registrados (GET /animales)
    2. Crear un nuevo animal (POST /animales)
    3. Salir

Autor: [Tu Nombre]
Fecha: [Fecha Actual]
"""
import os
import requests
import sys

URL_BASE = os.getenv("API_URL", "http://127.0.0.1:5000")

def ver_animales():
    """
    Realiza una petición GET a /animales para obtener la lista de animales.
    Muestra los resultados por pantalla.
    """
    try:
        r = requests.get(f"{URL_BASE}/animales")
        if r.status_code == 200:
            lista = r.json()
            if lista:
                print("\nLista de animales registrados:")
                for i, animal in enumerate(lista, 1):
                    print(f"{i}. {animal['tipo']} | Nombre: {animal['nombre']} | Edad: {animal['edad']} | Chip: {animal['chip']}")
            else:
                print("\nNo hay animales registrados aún.")
        else:
            print(f"Error al obtener animales. Código: {r.status_code}, Respuesta: {r.text}")
    except requests.RequestException as e:
        print(f"Ocurrió un error de conexión: {e}")

def crear_animal():
    """
    Pide datos por consola y hace un POST a /animales para crear un nuevo animal.

    Campos que envía en el JSON:
        - tipo (str)  : 'perro', 'gato', 'ave', 'pez'
        - nombre (str)
        - edad (int)
        - chip (str)  : opcional
        - raza (str)  : opcional, se usa en perro/gato
    """
    print("\n=== Crear Nuevo Animal ===")
    tipo = input("Tipo (perro, gato, ave, pez): ").strip().lower()
    nombre = input("Nombre: ").strip()
    try:
        edad = int(input("Edad (entero): ").strip())
    except ValueError:
        print("Edad no válida, se usará 0.")
        edad = 0

    chip = ""
    raza = ""
    if tipo in ("perro", "gato"):
        raza = input("Raza: ").strip()
        chip = input("Chip (si tiene, si no vacío): ").strip()

    data = {
        "tipo": tipo,
        "nombre": nombre,
        "edad": edad,
        "chip": chip,
        "raza": raza
    }

    try:
        r = requests.post(f"{URL_BASE}/animales", json=data)
        if r.status_code == 200:
            print(r.json().get("mensaje", "Animal creado correctamente."))
        else:
            print(f"Error al crear animal. Código: {r.status_code}, Respuesta: {r.text}")
    except requests.RequestException as e:
        print(f"Ocurrió un error de conexión: {e}")

def menu():
    """
    Muestra un menú básico en consola para elegir:
        1. Ver animales
        2. Crear animal
        3. Salir
    """
    while True:
        print("\n=== MENÚ DE EJEMPLOS API ===")
        print("1. Ver animales registrados")
        print("2. Crear un nuevo animal")
        print("3. Salir")

        opcion = input("Elige una opción: ")
        if opcion == '1':
            ver_animales()
        elif opcion == '2':
            crear_animal()
        elif opcion == '3':
            print("Saliendo del script...")
            sys.exit(0)
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    
    menu()
