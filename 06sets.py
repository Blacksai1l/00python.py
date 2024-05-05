#### sets ####
"""
los sets no son estructuras ordenadas a diferencia de las listas o las tuplas
un set no admite elementos repetidos
"""


mi_set= set()
mi_otro_set= {}
print (type (mi_set))
print (type (mi_otro_set)) #sin datos dice que es un diccionario

mi_otro_set= {36 , 1.81, "Manu" , "Castilla"}
print (type (mi_otro_set)) # con datos si dice que es un set
print (len(mi_otro_set)) # mi set tiene 4 elementos
# print(mi_otro_set[1]) TypeError: 'set' object is not subscriptable

### operaciones en los sets ###


print(mi_otro_set)
mi_otro_set.add("verde")
print(mi_otro_set) # un set no es una estructura ordenada
mi_otro_set.add("Manu")
print(mi_otro_set) #un set no permite elementos repetidos

#tenemos la posibilidad de realizar busquedas dentro del set
print("Manu" in mi_otro_set)
print("Mani" in mi_otro_set)

#tambien podemos eliminar elementos del set
mi_otro_set.remove("verde")
print(mi_otro_set)
#tambiém podemos elimitar el set
mi_otro_set.clear()
print(mi_otro_set)
print(len(mi_otro_set))

#defino otros sets
mi_otro_set = {"manu", "castilla", 1.81, 37}
mi_set={1,2,3,4,5,6,7,8,9}
print(mi_set)
#del mi_set
#print (mi_set) NameError: name 'mi_set' is not defined
#del mi_set[1]
#print (mi_set) TypeError: 'set' object doesn't support item deletion

#actualizar un dato del set

print (type(mi_set))
mi_lista=list (mi_set)
print (type(mi_lista))
del mi_lista [0]
print(mi_lista)
mi_nuevo_set=set (mi_lista)
print (type(mi_nuevo_set))

#podemos juntar sets
mi_set_unido=mi_set.union(mi_nuevo_set)
print(mi_set_unido)
print(len(mi_set_unido))
print(type(mi_set_unido))

#otro ejemplo
mi_set_unido=mi_otro_set.union(mi_nuevo_set)
print(mi_set_unido)
print(len(mi_set_unido))
print(type(mi_set_unido))
#otro ejemplo
mi_set_unido=mi_otro_set.union(mi_nuevo_set).union({"verde", "real_betis"})
print(mi_set_unido)
print(len(mi_set_unido))
print(type(mi_set_unido))

# podemos saber las difernecias entre dos sets
print (mi_otro_set)
print (mi_set_unido)
print (mi_set_unido.difference(mi_otro_set))