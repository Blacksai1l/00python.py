from fastapi import FastAPI

app = FastAPI ()

@app.get ("/")
async def root (): 
    """siempre que llamamos a un servidor la funcion tiene que ser asincrona. async. 
    Todas las aplicaciones que estan en un servidor estan asincronicas de manera 
    default hasta que necesitan sincronizarse"""
    return "hola, FasAPI!"

# vamos ahora a levantar el servidos que nos proporciona fastapi
