### dar de alta un usuario ###

from fastapi import FastAPI
from pydantic import BaseModel # nos da la capacida de crear un model base al crear una clase

app = FastAPI ()

@app.get ("/usuariosjson") 
async def usuariojson (): 
    return [ {"nombre" :  "Antoñito", "apellido" : "Melano" , "contraseña" : "1234" , "edad" : 35},
             {"nombre" : "Manolito" , "apellido" : "Elpijo" , "contraseña" : "4321" , "edad" : 30},
             {"nombre" : "Luisito" , "apellido" : "Xantrea" , "contraseña" : "951357" , "edad" : 33}]

# levantar server con uvicorn usuarios:app --reload

# vamos a hacerlo mas facil
# creamos una clase

class usuario_clase  (BaseModel):
    id: int
    nombre: str
    apellido: str
    contraseña: str
    edad: int

#definimos una variable que es una lista con mis usuarios en funcion de la clase que he definido
listaUsuarios = [usuario_clase  (id = 1, nombre="Antoñito" , apellido="Melano", contraseña="1234", edad = 35),
                 usuario_clase  (id = 2 , nombre="Manolito" , apellido="Elpijo", contraseña="4321", edad = 30),
                 usuario_clase  (id = 3 , nombre="Luisito" , apellido="Xantrea", contraseña="951357", edad = 33),]

# aqui nos va a devolver a todos los usuarios en http://127.0.0.1:8000/usuarios
@app.get("/usuarios")
async def usuarios():
    return listaUsuarios

# aqui nos va a devolver solo el usario que le pidamso en http://127.0.0.1:8000/usuario/1 o 2 o 3
# path
@app.get("/usuario/{id}")
async def usuario_clase (id: int):
    usuarios = filter (lambda usuario: usuario.id == id, listaUsuarios)
    try: 
        return list (usuarios)[0]
    except: 
        return {"error" : " No se ha encontrado el usuario"}

# query
"""
que significa llamar a un parametro por Query?
Lo que significa es  igualar una clave a una url
"""
# aqui nos va a devolver solo el usario que le pidamso en http://127.0.0.1:8000/usuarioquery/?id= 1 o  2 o 3 ...

@app.get("/usuarioquery/")
async def usuario_clase (id: int):
    usuarios = filter (lambda usuario: usuario.id == id, listaUsuarios)
    try: 
        return list (usuarios)[0]
    except: 
        return {"error" : " No se ha encontrado el usuario"}
    

# ahora definimos una función para que el codigo quede mas limpio. 

def busquedausario (id:int):
    usuarios = filter (lambda usuario: usuario.id == id, listaUsuarios)
    try: 
        return list (usuarios)[0]
    except: 
        return {"error" : " No se ha encontrado el usuario"}

#por path
@app.get("/usuario/{id}")
async def usuario_clase (id: int):
    return busquedausario(id)

# por query
@app.get("/usuarioquery/")
async def usuario_clase (id: int):
    return busquedausario(id)



"""
se suele usar el path cuando consideramos que es 1 parametro fijo, ejempo usuario y placa del coche
se suele usar el query cuando consideramos que el parametro no es obligatorio para hacer la petición ejemplo
la placa del coche que termine en tal.

"""

### AÑADIR NUEVOS USUARIOS ####
"""
USAREMOS EL @APP.POST
"""

@app.post ("/usuario")
async def nuevoUsuario ( usuario : usuario_clase):
    #if type ( busquedausario ( usuario.id )) == usuario_clase :
    #    return {"error" , "el usuario ya existe"}
    #else: 
        listaUsuarios.append (usuario)
    

