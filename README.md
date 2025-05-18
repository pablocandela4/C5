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

## Instrucciones de instalación

1. Clona este repositorio:
```bash
git clone [https://github.com/pablocandela4/C5.git](https://github.com/pablocandela4/C5.git)
cd C5-main
```

2. Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```

3. Verifica que exista el archivo de base de datos en datos/clinica.db.

---

## Estructura del proyecto

- `animales/`: Definición de las clases base para animales (perros, gatos, peces, aves) y gestión de propietarios.
- `alimentacion/`: Gestión de alimentos disponibles, historial de alimentación y ventas.
- `cuidados/`: Registro y gestión de cuidados específicos según el tipo de animal.
- `salud/`: Gestión de tratamientos, vacunaciones y consultas veterinarias.
- `interfaz/`: Módulos para los menús de la interfaz de usuario.
- `database/`: Conexión y gestión con base de datos MySQL.
- `api/`: API básica para exponer algunas funcionalidades.
- `datos/`: Contiene la base de datos SQLite utilizada por defecto (`clinica.db`).
- Scripts auxiliares:
  - `ejemplo.py`: Script de ejemplo para probar funcionalidades.
  - `probar.py`: Script para pruebas rápidas.
  - `test_db.py`: Pruebas relacionadas con la base de datos.
 
---

## Uso

Puedes ejecutar el sistema completo desde el menú principal:
```bash
python interfaz/menu_principal.py
```
También puedes probar partes específicas del sistema usando los scripts incluidos, como `ejemplo.py` o `probar.py`.

---

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.
