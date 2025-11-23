from flask import Flask, jsonify
from services.openbank_api import get_openbank_data

app = Flask(__name__)

# Página principal para GoCardless
@app.route('/')
def home():
    return "¡Backend funcionando en localhost:5000!"

# Callback para GoCardless
@app.route('/callback')
def callback():
    return "¡Callback de GoCardless recibido!"

# Tu ruta actual de datos
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
    # Añadimos host="0.0.0.0" si quieres que ngrok pueda conectarse
    app.run(debug=True, port=5000, host="0.0.0.0")

