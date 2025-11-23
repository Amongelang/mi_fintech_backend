# services/openbank_api.py
import requests

# Base URL de GoCardless Open Banking (sandbox / live)
BASE_URL = "https://api.gocardless.com/openbanking"  # Reemplaza si la doc oficial indica otra
TOKEN = "live_J4dyY9hEMDoSmtfnRP6JfJUHj_G3d8ixvrSCLe-V"  # Tu token

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def get_openbank_data():
    """
    Función que obtiene los datos de cuentas, saldo y transacciones.
    De momento devuelve datos simulados, luego puedes reemplazar con
    llamadas reales a la API de GoCardless/Nordigen.
    """
    try:
        # Ejemplo de llamada real (descomentar cuando tengas endpoints correctos)
        # resp_accounts = requests.get(f"{BASE_URL}/accounts", headers=HEADERS)
        # accounts = resp_accounts.json()
        #
        # resp_transactions = requests.get(f"{BASE_URL}/transactions", headers=HEADERS)
        # transactions = resp_transactions.json()
        #
        # balance_total = sum([acc["balance"] for acc in accounts])

        # Datos simulados para pruebas
        accounts = [
            {
                "name": "Cuenta de prueba",
                "balance": 1000,
                "currency": "EUR"
            }
        ]
        transactions = [
            {"date": "2025-11-23", "amount": -50, "description": "Gasto de prueba"},
            {"date": "2025-11-22", "amount": 200, "description": "Ingreso de prueba"}
        ]
        total_balance = sum(acc["balance"] for acc in accounts)

        return {
            "accounts": accounts,
            "transactions": transactions,
            "balance": total_balance
        }

    except Exception as e:
        # Para no romper el backend si falla algo
        print(f"Error al obtener datos de OpenBank: {e}")
        return {
            "accounts": [],
            "transactions": [],
            "balance": 0
        }
