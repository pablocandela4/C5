"""
menu_animales.py

Módulo que gestiona la interacción de usuario para crear, listar y administrar
animales (Perro, Gato, Ave, Pez) dentro de la aplicación. NO depende de ninguna
carpeta acceso_datos. Almacena los animales en una lista local en memoria.


"""


from animales.animal import Perro, Gato, Ave, Pez
from database import db



def menu_animales():
    while True:
        print("\n--- MENÚ ANIMALES ---")
        print("1. Listar")
        print("2. Registrar")
        print("3. Editar")
        print("4. Eliminar")
        print("0. Volver")
        opc = input("> ")

        if opc == "1":
            for a in db.get_animales():
                print(f"{a['id']:3} - {a['tipo']} {a['nombre']} ({a['edad']} a)")
        elif opc == "2":
            datos = {
                "tipo": input("Tipo: "),
                "nombre": input("Nombre: "),
                "edad": int(input("Edad: ")),
                "chip": input("Chip: "),
                "raza": input("Raza: "),
            }
            db.insert_animal(datos)
            print("✓ Registrado")
        elif opc == "3":
            _id = int(input("ID a editar: "))
            campo = input("Campo (nombre/edad/raza/chip): ")
            valor = input("Nuevo valor: ")
            db.update_animal(_id, {campo: valor})
            print("✓ Actualizado")
        elif opc == "4":
            _id = int(input("ID a eliminar: "))
            db.delete_animal(_id)
            print("✓ Eliminado")
        elif opc == "0":
            break