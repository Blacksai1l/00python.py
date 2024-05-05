### Diccionarios ####
"""
Son datos o claves asociados a un valor
Es lo que conocemos como un json
"""
mi_diccionario=dict()
mi_otro_diccionario={}
print(type(mi_diccionario))
print(type(mi_otro_diccionario))

mi_otro_diccionario= {"Nombre": "Manu" , "Apellido":"Castilla", "Edad" : 37 , "Altura" :1.81}
print(type(mi_otro_diccionario))
print(mi_otro_diccionario)

mi_diccionario ={
    "equipo": "Real betis",
    "color": "verde",
    "lenguajes": {"pythom", "Swift", "Kotlin"}
    }
print(mi_diccionario)
print(len(mi_diccionario))
print(len(mi_otro_diccionario))

print(mi_diccionario["equipo"])

##  operaciones con diccionarios ##

#añadir elementos a un diccionario
mi_diccionario["ciudad"] = "Sevilla"
print(mi_diccionario)
#modificar elementos
mi_diccionario["ciudad"] = "Huelva"
print(mi_diccionario)
# eliminar un elemento del diccionario 
del mi_diccionario["ciudad"]
print (mi_diccionario)
# comprobar si hay un elemento en mi diccionario 
print("Real betis" in mi_diccionario)
print("equipo" in mi_diccionario)#busca en los claves no en el valor

print(mi_diccionario.items())
print(mi_diccionario.keys())
print(mi_diccionario.values())
#crear un diccionario nuevo sin valores aprovechando las claves para despues irlo rellenado con nuevos valores 
mi_nuevo_diccionario = dict.fromkeys(mi_otro_diccionario)
print(mi_nuevo_diccionario)
mi_nuevo_diccionario["Nombre"]= "Antonio"
print(mi_nuevo_diccionario)
#meterle a las claves el mismo valor
mi_nuevo_diccionario=dict.fromkeys(mi_otro_diccionario,"Hola")
print(mi_nuevo_diccionario)

print()
### trasnformar el diccionario en lista , set , tupla etc
print(list(mi_nuevo_diccionario))
print(tuple(mi_nuevo_diccionario))
print(set(mi_nuevo_diccionario))