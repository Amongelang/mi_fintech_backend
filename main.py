from flask import Flask, jsonify
from services.openbank_api import get_openbank_data, get_institutions

app = Flask(__name__)

# Página principal
@app.route('/')
def home():
    return "¡Backend funcionando!"

# Ruta para obtener datos falsos de ejemplo
@app.route("/data")
def get_data():
    data_openbank = get_openbank_data()
    result = {
        "total_balance":  data_openbank['balance'],
        "accounts": [data_openbank],
        "transactions": data_openbank['transactions']
    }
    return jsonify(result)

# Ruta para listar bancos disponibles en Yapily
@app.route("/banks")
def banks():
    institutions = get_institutions()
    return jsonify(institutions)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
