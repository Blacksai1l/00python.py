### dar de alta un usuario ###

from fastapi import FastAPI

app = FastAPI ()

@app.get ("/usuarios") 
async def usuario (): 
    return "hola, Usuarios!"

# levantar server con uvicorn usuario:app --reload