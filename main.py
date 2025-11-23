@app.route("/data")
def get_data():
    result = {
        "total_balance": 1000,
        "accounts": [
            {"name": "Cuenta de prueba", "balance": 1000}
        ],
        "transactions": [
            {"date": "2025-11-23", "amount": -50, "description": "Gasto prueba"}
        ]
    }
    return jsonify(result)


