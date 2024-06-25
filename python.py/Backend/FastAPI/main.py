

"""siempre que llamamos a un servidor la funcion tiene que ser asincrona. async. 
Todas las aplicaciones que estan en un servidor estan asincronicas de manera 
default hasta que necesitan sincronizarse, si no imaginate el gasto de memoria """

from fastapi import FastAPI

app = FastAPI ()

@app.get ("/") # "/" se refieere a que pueda abrir cualquier fichero
async def root (): 

    return "hola, FasAPI!"

"""
vamos ahora a levantar el servidos que nos proporciona fastapi
para ello nos vamos en la consola al fichero donde estamos picando el proyectoç
en este caspo seria python.py/Backend/FastAPI
Despues metemos el comando: uvicorn main:app --reload

"""
@app.get ("/url")
async def url (): 
    return { "url" : "https://mouredev.com/python" } #esto lo ponemos en formato .json... en 
                                                     #en general la forma de la informacion en web es .json

# Documentacion de Swagger: http:127.0.0.1:8000/docs
# Documentacion de Redocly: http:127.0.0.1:8000/redoc

"""
Normalmente usas:

POST: para crear datos.
GET: para leer datos.
PUT: para actualizar datos.
DELETE: para borrar datos.
"""