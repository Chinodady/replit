from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Catálogo de ejemplo (en memoria)
AUTOS = [
    {"id": 1, "marca": "Toyota",  "modelo": "Corolla", "anio": 2020, "precio": 285000, "color": "blanco"},
    {"id": 2, "marca": "Nissan",  "modelo": "Sentra",  "anio": 2019, "precio": 265000, "color": "gris"},
    {"id": 3, "marca": "Honda",   "modelo": "Civic",   "anio": 2021, "precio": 345000, "color": "rojo"},
    {"id": 4, "marca": "Mazda",   "modelo": "3",       "anio": 2018, "precio": 235000, "color": "negro"},
    {"id": 5, "marca": "Chevrolet","modelo": "Onix",   "anio": 2022, "precio": 315000, "color": "azul"},
]

@app.get("/api/autos")
def listar_autos():
    """GET /api/autos
    Filtros opcionales (query params):
      - marca, modelo, color  (texto exacto, case-insensitive)
      - anio_min, anio_max    (int)
      - precio_max            (int)
    """
    marca      = request.args.get("marca", type=str)
    modelo     = request.args.get("modelo", type=str)
    color      = request.args.get("color", type=str)
    anio_min   = request.args.get("anio_min", type=int)
    anio_max   = request.args.get("anio_max", type=int)
    precio_max = request.args.get("precio_max", type=int)

    def ok(a):
        def ieq(field, val):
            return (val is None) or (str(a[field]).lower() == val.lower())
        if not ieq("marca", marca):   return False
        if not ieq("modelo", modelo): return False
        if not ieq("color", color):   return False
        if anio_min is not None and a["anio"] < anio_min:   return False
        if anio_max is not None and a["anio"] > anio_max:   return False
        if precio_max is not None and a["precio"] > precio_max: return False
        return True

    filtrados = [a for a in AUTOS if ok(a)]
    return jsonify({"total": len(filtrados), "items": filtrados})

@app.get("/api/autos/<int:auto_id>")
def detalle_auto(auto_id):
    for a in AUTOS:
        if a["id"] == auto_id:
            return jsonify(a)
    return jsonify({"error": "Auto no encontrado"}), 404

@app.get("/")
def root():
    return jsonify({"status": "ok", "servicio": "catalogo-autos"})

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
