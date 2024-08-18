# main.py
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/api/tokens")
async def get_tokens():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.v2.tibetswap.io/tokens")
        tokens = response.json()
    return tokens

# Para ejecutar: uvicorn main:app --reload