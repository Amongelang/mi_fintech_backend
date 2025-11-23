from flask import Flask, jsonify

# Definir la app antes de los endpoints
app = Flask(__name__)

# Endpoint raíz
@app.route("/")
def home():
    return "¡Backend funcionando en localhost:5000!"

# Endpoint /data con datos de prueba
@app.route("/data")
def get_data():
    # Datos de prueba, simulando la estructura que luego vendrá de tus APIs reales
    result = {
        "total_balance": 1000,
        "accounts": [
            {
                "name": "Cuenta de prueba",
                "balance": 1000,
                "currency": "EUR"
            }
        ],
        "transactions": [
            {
                "date": "2025-11-23",
                "amount": -50,
                "description": "Gasto de prueba"
            },
            {
                "date": "2025-11-22",
                "amount": 200,
                "description": "Ingreso de prueba"
            }
        ]
    }
    return jsonify(result)

# Esto permite ejecutar la app localmente
if __name__ == "__main__":
    app.run(debug=True)


