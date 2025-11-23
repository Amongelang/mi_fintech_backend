from nordigen import NordigenClient

# Tus credenciales Nordigen (regístrate gratis en https://nordigen.com/)
SECRET_ID = "TU_SECRET_ID"
SECRET_KEY = "TU_SECRET_KEY"

client = NordigenClient(secret_id=SECRET_ID, secret_key=SECRET_KEY)

def get_openbank_data():
    # 1. Lista de cuentas
    accounts = client.get_requisitions()  # más adelante, puedes filtrar tu cuenta específica

    # 2. Para simplificar, devolvemos datos de ejemplo
    # En la práctica se reemplaza por la info real del usuario
    data = {
        "balance": 1234.56,
        "transactions": [
            {"title": "Sueldo", "amount": 1200.00},
            {"title": "Supermercado", "amount": -45.50},
            {"title": "Netflix", "amount": -15.99}
        ],
        "name": "OpenBank"
    }
    return data
