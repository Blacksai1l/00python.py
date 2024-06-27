# CREAMOS LA API

from fastapi import FastAPI


app = FastAPI ()

@app.get ("/")
def raiz ():
    return  { " mensaje" : "hola fastapi " }

"""
@app.get ("/")
def raiz2 ():
    return  { " mensaje" : "hola fastapi 2" }

no va a funcionar porque se lo estmaos poniendo otra vez en la raiz 

"""

# Inicia el server: uvicorn users:app --reload
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

# PATH 
@app.get ("/2")
def raiz2 ():
    return  { " mensaje" : "hola fastapi 2" }

@app.get ("/me")
def miusurio ():
    return  { " mensaje" : "usuario actual " }



"""
from pydantic import BaseModel

class Usuario (BaseModel):
    id: int
    nombre: str
    apellido: str
    edad: int
"""