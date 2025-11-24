import requests
from requests.auth import HTTPBasicAuth
import os

BASE_URL = "https://api.yapily.com"

CLIENT_ID = os.getenv("YAPILY_CLIENT_ID")
CLIENT_SECRET = os.getenv("YAPILY_CLIENT_SECRET")


def get_access_token():
    """Obtiene un token de acceso de Yapily usando client_id y client_secret."""
    url = f"{BASE_URL}/oauth/token"
    payload = {"grant_type": "client_credentials"}
    
    response = requests.post(url, json=payload, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
    
    if response.status_code != 200:
        print("Error al obtener token:", response.text)
        return None
    
    return response.json().get("access_token")

def get_yapily_banks():
    token = get_access_token()
    if not token:
        return {"error": "No se pudo obtener token"}

    url = f"{BASE_URL}/institutions"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "user-agent": "MiFintechApp/1.0",
    }
    params = {"country": "ESP"}  # Solo España
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return {"error": "No se pudo obtener la lista de bancos", "status": response.status_code}

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
