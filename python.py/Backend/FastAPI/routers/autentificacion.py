from fastapi import FastAPI 
from pydantic import BaseModel

app= FastAPI()

# uvicorn autentificacion:app --reload



class Usuario (BaseModel):
    id: int
    nombre: str
    apellido: str
    contraseña : str
    edad: int