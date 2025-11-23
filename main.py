from flask import Flask, jsonify
from services.openbank_api import get_openbank_data, get_yapily_banks

app = Flask(__name__)

# Página principal
@app.route('/')
def home():
    return "¡Backend funcionando en localhost:5000!"

# Callback para GoCardless (lo puedes mantener aunque no uses Nordigen)
@app.route('/callback')
def callback():
    return "¡Callback de GoCardless recibido!"

# Ruta para obtener los bancos disponibles desde Yapily
@app.route("/banks")
def banks():
    banks_list = get_yapily_banks()
    return jsonify(banks_list)

# Ruta de datos (cuentas y transacciones)
@app.route("/data")
def get_data():
    data_openbank = get_openbank_data()
    result = {
        "total_balance":  data_openbank['balance'],
        "accounts": [data_openbank],
        "transactions": data_openbank['transactions']
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
