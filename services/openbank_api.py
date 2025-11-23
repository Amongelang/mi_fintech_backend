import os
import requests
from datetime import date

# URL base de la API de GoCardless (antes Nordigen)
BASE_URL = "https://api.gocardless.com"

# Token seguro desde variable de entorno
API_TOKEN = os.environ.get("GOCARDLESS_TOKEN")

def get_openbank_data():
    """
    Función de ejemplo que simula la llamada a la API de GoCardless
    y devuelve los datos en el mismo formato que tenías antes.
    """
    
    # Si quisieras hacer llamadas reales:
    # headers = {"Authorization": f"Bearer {API_TOKEN}"}
    # response = requests.get(f"{BASE_URL}/endpoint_que_necesites", headers=headers)
    # data = response.json()
    
    # Por ahora, datos de prueba
    data = {
        "balance": 1000,
        "currency": "EUR",
        "name": "Cuenta de prueba",
        "transactions": [
            {"amount": -50, "date": str(date.today()), "description": "Gasto de prueba"},
            {"amount": 200, "date": str(date.today()), "description": "Ingreso de prueba"},
        ]
    }
    
    return data

