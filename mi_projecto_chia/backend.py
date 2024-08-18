from fastapi import FastAPI
import httpx
import json

app = FastAPI()

@app.get("/api/tokens")
async def get_tokens():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.v2.tibetswap.io/tokens")
        tokens = response.json()
    print(json.dumps(tokens, indent=2))  # Imprime la estructura de los datos de forma legible
    return tokens

# Para ejecutar: uvicorn backend:app --reload