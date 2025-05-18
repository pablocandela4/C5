import os
from .db_base import get_db_manager

# Instancia global que usa la factoría de db_base
db = get_db_manager()
