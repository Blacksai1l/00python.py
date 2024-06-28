

"""siempre que llamamos a un servidor la funcion tiene que ser asincrona. async. 
Todas las aplicaciones que estan en un servidor estan asincronicas de manera 
default hasta que necesitan sincronizarse, si no imaginate el gasto de memoria """

from fastapi import FastAPI
from routers import productos , usuarios 




app = FastAPI ()

# Routers 
app.include_router(productos.router)
app.include_router(usuarios.router)

@app.get ("/") # "/" se refieere a que pueda abrir cualquier fichero
async def root (): 

    return "hola, FasAPI!"

"""
vamos ahora a levantar el servidos que nos proporciona fastapi
para ello nos vamos en la consola al fichero donde estamos picando el proyectoç
en este caspo seria python.py/Backend/FastAPIc
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

### RECURSOS ESTATICOS 
"""
es un recurso imagen, pdf... lo que sea que siempre va a estar en el servidor disponible 
creamos una carpeta que se llama statics y dentro un archivo llamado imagenes
donde vamos a guardar las imagenes que queramos.
Para que estas imagenes esten diponibles mediante el path 

"""
from fastapi.staticfiles import StaticFiles
app.mount("/statics", StaticFiles (directory="statics") , name= "statics")

#La imagen está en --->  http://127.0.0.1:8000/statics/images/simbolo del dolar.png
# 


"""
##### COOKIE PARAMETERS 
#You can define Cookie parameters the same way you define Query and Path parameters.

# Import Cookie
# First import Cookie:

from typing import Annotated
from fastapi import Cookie, FastAPI
app = FastAPI()

# Declare Cookie parameters

@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}

##### HEADER PARAMETER

# import header
from typing import Annotated
from fastapi import FastAPI, Header


# Declare Header parameters
@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}

"""