import requests
import os
import json   

# Lee la variable de entorno; si no existe usa localhost
BASE = os.getenv("API_URL", "http://127.0.0.1:5000")
print("BASE =", BASE)

# 1. Insertar
nuevo = {"tipo": "ave", "nombre": "Piolín", "edad": 1}
r = requests.post(f"{BASE}/animales", json=nuevo)
print("POST:", r.status_code)
print(r.text)  


# 2. Listar
r = requests.get(f"{BASE}/animales")
print("GET:", r.status_code)
print(r.text) 

# 3. Actualizar (id = 1)
r = requests.put(f"{BASE}/animales/1", json={"edad": 2})
print("PUT:", r.status_code)
print(r.text) 

# 4. Borrar
r = requests.delete(f"{BASE}/animales/1")
print("DELETE:", r.status_code)
print(r.text) 
