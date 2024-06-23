#####CLASES#####    
"""
poder identificar nuestro codigo dentro de un hambito
los nombres de las clases se prefiere poner la primera letra de cada palabra en 
mayusculas todo junto y sin espacios
Las clases pueden hacer cosas, pueden tener contructores que necesitan parametros
"""

class MyEmptyPerson :
    pass
print(MyEmptyPerson)

#para crear la clase con dos constructores

class Person:
    def __init__(self, name, surname):
        self.name= name
        self.surname= surname

mi_persona= Person("Manu", "Castilla")
print(mi_persona.name)
print(mi_persona.surname)
print (f"{mi_persona.name} {mi_persona.surname}")

#otra forma de hacerlo con un solo constructor#
class Person:
    def __init__(self, name, surname, alias = "sin alias"): #estamos definiendo el constructor
        self.full_name= f" {name}  {surname} {alias}"
        self.__name= name #propiedad privada. No la puedo midificar ni acceder a ella salvo si hago una fuincion con return

    def get_name (self):
        return self.__name
            
    def caminar(self):#estamos definiendo una funcion
        print(f"{self.full_name} está caminando")


mi_persona= Person("Manu" , "Castilla")        
print(mi_persona.full_name)
mi_persona.caminar()

mi_otra_persona=Person("Manu","Castilla", "@mojonario")
print(mi_otra_persona.full_name)
print (mi_otra_persona.get_name())
mi_otra_persona.caminar()

#puedo acceder a mi clase sin tener que volver a definir la clase

mi_otra_persona.full_name= "Antonio Contreras @pasakillo"
print(mi_otra_persona.full_name)

mi_otra_persona.caminar()
