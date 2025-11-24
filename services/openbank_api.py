import os
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://api.yapily.com"

APPLICATION_UUID = os.getenv("YAPILY_APPLICATION_UUID")
APPLICATION_SECRET = os.getenv("YAPILY_APPLICATION_SECRET")

HEADERS = {
    "Accept": "application/json",
    "user-agent": "MiFintechApp/1.0",
}


def get_yapily_banks():
    """Lista los bancos disponibles en España mediante Yapily."""
    url = f"{BASE_URL}/institutions"
    auth = HTTPBasicAuth(APPLICATION_UUID, APPLICATION_SECRET)
    params = {"country": "ESP"}  # Solo España
    response = requests.get(url, headers=HEADERS, params=params, auth=auth)

    if response.status_code != 200:
        return {"error": "No se pudo obtener la lista de bancos", "status": response.status_code, "text": response.text}

    return response.json().get("data", [])


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
