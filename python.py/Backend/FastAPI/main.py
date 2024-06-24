

"""siempre que llamamos a un servidor la funcion tiene que ser asincrona. async. 
Todas las aplicaciones que estan en un servidor estan asincronicas de manera 
default hasta que necesitan sincronizarse, si no imaginate el gasto de memoria """

from fastapi import FastAPI

app = FastAPI ()

@app.get ("/") # "/" se refieere a que pueda abrir cualquier fichero
async def root (): 

    return "hola, FasAPI!"

# vamos ahora a levantar el servidos que nos proporciona fastapi

@app.get ("/url")
async def url (): 
    return { "url" : "https://mouredev.com/python" } #esto lo ponemos en formato .json... en 
                                                     #en general la forma de la informacion en web es .json
