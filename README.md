# Gestión de Cuidados Veterinarios

Este módulo forma parte del sistema de gestión veterinaria y permite registrar, visualizar y actualizar cuidados programados para distintos tipos de animales. Incluye lógica específica para perros, gatos, aves y peces.

---

## Autores

* (Coordinador) [Lucas Beneyto Sánchez-Sarachaga](https://github.com/lucasbeneyto)
* [Pablo Candela Ortega](https://github.com/pablocandela4) ← Responsable del módulo de cuidados
* [Úrsula Guillo Orts](https://github.com/u1159)
* [Miguel Pérez Alonso](https://github.com/mpa113)
* [Alejandro Paco García](https://github.com/apg260)

---

## Profesorado

[//]: # ([Cristina Cachero](https://github.com/ccacheroc))
[Miguel A. Teruel](https://github.com/materuel-ua) / [Cristina Cachero](https://github.com/ccacheroc)

---

## Requisitos

* Python 3.8 o superior
* Carpeta `datos/` existente para almacenar el archivo `cuidados.csv`
* Módulos importables dentro del directorio `logica/cuidados/`

---

## Instrucciones de instalación y uso

1. Asegúrate de que existe la carpeta `datos/`.
2. Importa las clases y funciones desde el paquete `logica.cuidados`.
3. Utiliza las funciones como `guardar_cuidados`, `cargar_cuidados`, `mostrar_cuidados`, etc.
4. Si se integra con la API o un menú, estas funciones deben ser llamadas desde los controladores correspondientes.

---

## Descripción del módulo

Este módulo permite:

- Programar cuidados médicos, de higiene o mantenimiento para animales.
- Personalizar el tipo de cuidado según el tipo de animal (perro, gato, ave, pez).
- Guardar y cargar cuidados desde un archivo CSV (`cuidados.csv`).
- Cambiar el estado de un cuidado (`pendiente`, `realizado`, `cancelado`).
- Buscar cuidados asociados a un animal concreto.

---

## Estructura del código

