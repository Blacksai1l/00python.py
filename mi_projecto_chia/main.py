from fastapi import FastAPI, Query
import requests

app = FastAPI()

DEXIE_API_URL = "https://api.dexie.space/v2/prices/pairs"
DEXIE_API_URL2 = "https://api.dexie.space/v2/prices/tickers"

@app.get("/tokens")
def get_chia_tokens(base: str = Query(None, description="Base del token para filtrar")):
    """
    Consulta la lista de tokens CATS desde la API de Dexie y filtra por el campo 'base' si se proporciona.
    """
    try:
        response = requests.get(DEXIE_API_URL)
        response.raise_for_status()  # Asegurarse de que la solicitud fue exitosa
        tokens = response.json()

        if base:
            # Filtrar tokens por base (case-insensitive)
            filtered_tokens = [token for token in tokens if token['base'].lower() == base.lower()]
            return filtered_tokens if filtered_tokens else {"error": f"No se encontró ningún token con base '{base}'."}

        return tokens  # Devuelve todos los tokens si no se proporciona un filtro
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    
@app.get("/prices")
def get_chia_prices():
    """
    Consulta la lista de precios de tokens desde la API de Dexie.
    """
    try:
        response = requests.get(DEXIE_API_URL2)
        response.raise_for_status()
        prices = response.json()
        return prices
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
