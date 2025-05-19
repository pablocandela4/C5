import os
from dotenv import load_dotenv

# Carga variables de entorno (opcionalmente .env)
load_dotenv()

# Importa tu app Flask
from api.app import app

if __name__ == "__main__":
    # Por defecto escucha en el puerto 5000 y localhost
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
