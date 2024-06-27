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

# Inicia el server: uvicorn usuarios:app --reload
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

# PATH 
@app.get ("/2")
def raiz2 ():
    return  { " mensaje" : "hola fastapi 2" }

@app.get ("/me")
def miusurio ():
    return  { " mensaje" : "usuario actual" }


from pydantic import BaseModel

class Usuario (BaseModel):
    id: int
    nombre: str
    apellido: str
    contraseña : str
    edad: int

usuarios_db= [Usuario (id = 1 , nombre= "Cabesa" , apellido= "Porta" , contraseña= "5" , edad= 30),
              Usuario (id= 2, nombre= "Migue" , apellido= "Suarez" , contraseña= "5premio" ,edad= 31),
              Usuario (id= 3, nombre= "Antonio" , apellido= "Huerta" , contraseña= "55premios" ,edad= 32)]

@app.get ("/usuariosoriginal")
def totaldeusuariosoriginal ():
    return [
 {"id": 1,"nombre": "Cabesa","apellido": "Porta","contraseña": "5","edad": 30}, 
 {"id": 2,"nombre": "Migue","apellido": "Suarez","contraseña": "5premio","edad": 31},
 {"id": 3,"nombre": "Antonio ","apellido": "Huerta","contraseña": "55premios","edad": 32}
 ] 

@app.get ("/usuarios")
def totaldeusuarios ():
    return usuarios_db 

"""
@app.get ("/usuariosdb")
def userclass ():
    return Usuario (id = 1 , nombre= "Cabesa" , apellido= "Porta" , contraseña= "5" , edad= 30)
"""

@app.get ("/usuariosdb")
def userclass ():
    return usuarios_db

#llamar por path
#http://127.0.0.1:8000/usuario/1

@app.get ("/usuario/{id}")
def userid (id: int):
    miusuario= filter  ( lambda usuario : usuario.id == id , usuarios_db ) 
    try:
        return list (miusuario)[0]
    except:
        return {"error" : "No se ha encontrado el usuario con esa id "}
    
#llamar por query
#http://127.0.0.1:8000/userquery/?id=1

"""
recuerdo de la funcion filter
filter es una funcion de orden superior que filtra una lista iterable y devulver otra lista
su estructura es asi --> filter(lambda numero: numero > 10 ,numeros)
donde numetos es mi lista a la que le paso el filtro;
el filtro es numero > 10
numero: es el parametro  
de una lista de numeros, me hace otra lista con los numeros que sea mayor de 10
"""
@app.get ("/userquery/")
def useridquery (id: int):
    miusuario= filter  ( lambda usuario : usuario.id == id , usuarios_db ) 
    try:
        return list (miusuario)[0]
    except:
        return {"error" : "No se ha encontrado el usuario con esa id "}  
    
# añadir usuario a mi db
# http://127.0.0.1:8000/nuevousuario y rellenar la parte del cuerpo requerido en formato json
@app.post ("/nuevousuario/")
async def addusuario (usuario1: Usuario):
    usuarios_db.append (usuario1)
    return usuario1 # si no ponemos esto sigue funcionando pero nos devuelve un null
    
#actualizar un usuario de mi db 
# http://127.0.0.1:8000/cambiousario
@app.put ("/cambiousario/")
async def cambiousuario (usuario2 : Usuario):
    usuariodb : Usuario
    encontrado= False
    for indice, usuariodb in enumerate (usuarios_db):
        if usuariodb.id == usuario2.id:
            encontrado= True
            usuarios_db[indice] = usuario2
             
            
    if not encontrado:
        return {"error" : "El usuario a modificar no se encuentra en el listado"}
    else:
        return usuario2

# borrar un usuario de mi db
# http://127.0.0.1:8000/borrarusuario/4 (se borra el usuario 4 de mi base de datos)
@app.delete ("/borrarusuario/{id}")
async def borrarusuario (id: int):
    for indice, usuariodb in enumerate (usuarios_db):
        
        encontrado= False

        if usuariodb.id == id:
            encontrado= True
            del usuarios_db[indice]

    if not encontrado:
        return {"error" : "no se ha podido borrar porque el usuario no existe"}
            
        
