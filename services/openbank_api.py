import os
import requests

BASE_URL = "https://api.yapily.com"

CLIENT_ID = os.getenv("YAPILY_CLIENT_ID")
CLIENT_SECRET = os.getenv("YAPILY_CLIENT_SECRET")

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "user-agent": "MiFintechApp/1.0",
}

def get_yapily_banks():
    """Lista los bancos disponibles en España mediante Yapily."""
    url = f"{BASE_URL}/institutions"
    response = requests.get(url, headers=HEADERS, auth=(CLIENT_ID, CLIENT_SECRET))

    if response.status_code != 200:
        return {"error": "No se pudo obtener la lista de bancos"}, response.status_code

    institutions = response.json().get("data", [])
    return institutions


def get_openbank_data():
    """
    Función provisional para devolver datos falsos.
    Cuando conectemos a un banco real, se reemplaza por la lógica de Yapily.
    """

    fake_account = {
        "name": "Cuenta de prueba",
        "balance": 1000,
        "currency": "EUR",
        "transactions": [
            {
                "description": "Gasto de prueba",
                "amount": -50,
                "date": "2025-11-23"
            },
            {
                "description": "Ingreso de prueba",
                "amount": 200,
                "date": "2025-11-23"
            }
        ]
    }

    return fake_account
