# test_db.py
from database.db_base import get_db_manager

def main():
    db = get_db_manager()
    animales = db.get_animales()  # debe funcionar aunque la tabla esté vacía
    print("✅ Conexión OK, animales:", animales)

if __name__ == "__main__":
    main()
