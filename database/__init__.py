"""
Fábrica sencilla: importa una variable de entorno DB_BACKEND
('sqlite' | 'mysql') y devuelve la instancia adecuada, accesible como
`database.db`.
"""
# database/__init__.py
import os
from .sqlite_manager import SQLiteManager
from .mysql_manager   import MySQLManager

def db():
    backend = os.getenv("DB_BACKEND", "sqlite")
    if backend == "mysql":
        return MySQLManager()
    else:
        return SQLiteManager()

db = db()   # instancia global usada en app.py
