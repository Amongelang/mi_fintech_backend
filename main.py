# main.py
from flask import Flask, jsonify
from services.openbank_api import get_openbank_data, get_yapily_banks

app = Flask(__name__)

# Página principal
@app.route('/')
def home():
    return "¡Backend funcionando en localhost:5000!"

# Callback (puedes usarlo más tarde para OAuth o pagos)
@app.route('/callback')
def callback():
    return "¡Callback recibido!"

# Ruta de datos de prueba
@app.route("/data")
def get_data():
    data_openbank = get_openbank_data()
    result = {
        "total_balance":  data_openbank['balance'],
        "accounts": [data_openbank],
        "transactions": data_openbank['transactions']
    }
    return jsonify(result)

# Ruta para obtener bancos de Yapily
@app.route("/banks")
def get_banks():
    banks = get_yapily_banks()
    return jsonify(banks)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
