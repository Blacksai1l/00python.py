from fastapi import FastAPI
import requests

app = FastAPI()  # Esta es la instancia que uvicorn necesita encontrar

DEXIE_API_URL = "https://api.dexie.space/v1/price"

@app.get("/tokens")
def get_chia_tokens():
    """
    Consulta la lista de tokens CATS desde la API de Dexie.
    """
    try:
        response = requests.get(DEXIE_API_URL)
        response.raise_for_status()
        tokens = response.json()
        return tokens
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}