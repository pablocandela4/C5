# run_app.py
from flask import Flask
# … o bien import tu CLI …
from api.app import app

if __name__ == "__main__":
    # Para Flask:
    app.run(host="0.0.0.0", port=5000, debug=True)
    # —o— para tu CLI:
    # import api.examples; api.examples.menu()
