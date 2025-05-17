"""
Fábrica sencilla: importa una variable de entorno DB_BACKEND
('sqlite' | 'mysql') y devuelve la instancia adecuada, accesible como
`database.db`.
"""
import os
from .sqlite_manager import SQLiteManager
from .mysql_manager import MySQLManager

_BACKEND = os.getenv("DB_BACKEND", "sqlite").lower()

if _BACKEND == "mysql":
    db = MySQLManager()
else:
    db = SQLiteManager()
