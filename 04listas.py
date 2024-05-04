#### listas ####

mi_lista= list() #asi se difine una lista
mi_otra_lista= [] #asi también de define una lista
print(len(mi_lista))
print(len(mi_otra_lista))

mi_lista= [35,14,11,80,16,16]
print((mi_lista))
print(len(mi_lista))

mi_otra_lista=[37 ,1.81,  "Manu", "Castilla"]
print (type (mi_lista))
print (type (mi_otra_lista))

print (mi_otra_lista)
print (mi_otra_lista[0])
print (mi_otra_lista[1])
print (mi_otra_lista[2])
print (mi_otra_lista[3])
print (mi_otra_lista[-1])
print (mi_otra_lista[-2])
print (mi_otra_lista[-3])
print (mi_otra_lista[-4])
#print (mi_otra_lista[5]) indexerror
#print (mi_otra_lista[-5]) indexerror


### funciones que podemos hacer en una lista ###3


print (mi_otra_lista.count("Manu")) # cuantas veces se repite?
print (mi_lista.count(16))


edad, altura, nombre, apellido= mi_otra_lista
print(edad)
print(altura)
print(nombre)
print(apellido)

print (mi_lista+mi_otra_lista)
# print (mi_lista-mi_otra_lista) errortype
# print (mi_lista*mi_otra_lista) errortype
# print (mi_lista/mi_otra_lista) errortype

#añadir otro elemento al final de la lista
mi_otra_lista.append("Huelva")
print (mi_otra_lista)
#cambiar un elemento de la lista
mi_otra_lista[4]="Sevilla"
print(mi_otra_lista)
#añadir otro elemento en un punto determinado de la lista
mi_otra_lista.insert(2, "verde")
print (mi_otra_lista)
#eliminar un elemento de la lista
mi_otra_lista.remove("verde")
print (mi_otra_lista)
#quita el ultimo elemento de la lista 
mi_otra_lista.pop()
print (mi_otra_lista)
#quita un elemento concreto de la lista 
mi_otra_lista.pop(2)
print (mi_otra_lista)
### con la funcion pop me puedo quedar con el elemento que saco de la lista y guardarlo en una variable o en otra lista
print(mi_lista)
mi_elemento_pop= mi_lista.pop(2)
print(mi_elemento_pop)
#desaparecer un elemento de la lista
print (mi_lista)
del mi_lista [2]
print (mi_lista)
#copiar una lista en otra
mi_nueva_lista= mi_lista.copy()
#borrar un lista entera
mi_lista.clear()
print(mi_lista)
print(mi_nueva_lista)
#altarnar el orden de los elementos de la lista
mi_nueva_lista.reverse()
print(mi_nueva_lista)
#ordena una lista segun un criterio o por orden alfabetico por defecto
mi_nueva_lista.sort()
print(mi_nueva_lista)


####sublistas####
print (mi_nueva_lista)
print (mi_nueva_lista[0:1])
print (mi_nueva_lista[0:2])
print (mi_nueva_lista[0:3])
print (mi_nueva_lista[0:4])
print (mi_nueva_lista[1:2])
print (mi_nueva_lista[1:3])
print (mi_nueva_lista[1:4])
print (mi_nueva_lista[2:3])
print (mi_nueva_lista[2:4])
print (mi_nueva_lista[3:4])
