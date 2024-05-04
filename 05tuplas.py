####    tuplas ####
#una tupla es un conjunto de valores y se diferencia de una
#lista en que sus valores no se pueden cambiar, son inmutables
#y no se pueden añadir mas, es un conjunto de valores cerrados
#si se pueden recombinar
mi_tupla= tuple()
mi_otra_tupla= (12,60,78,65,12,11,9)
mi_tupla=(35, 1.81 ,"Manu" , "Castilla")
print (mi_tupla)
print(type(mi_tupla))
print(mi_tupla[1])
print(mi_tupla[-1])
#print(mi_tupla[5]) indexerror
#print(mi_tupla[-5]) indexerror

print(mi_tupla.count("manu"))
print(mi_tupla.count("Manu"))
print(mi_tupla.index(1.81))
print(mi_tupla.index("Castilla"))

#mi_tupla[1]= 2.10 --> no te le deja cambiar son valores inmutables
#print(mi_tupla)
print (mi_tupla+mi_otra_tupla)
mu_suma_tupla= mi_tupla+mi_otra_tupla
print (mu_suma_tupla)

#subtuplas o slice
print (mu_suma_tupla [0:6])
print (mu_suma_tupla [2:6])
print (mu_suma_tupla [4:6])
print (mu_suma_tupla [2:11])

#puedo convertir un tupla en una lista si necesito cambiar sus valores
print (type(mi_tupla))
mi_tupla=list (mi_tupla)
print (type(mi_tupla))

#y ahora si puedo cambiar un dato de la tupla o añadir etc
mi_tupla[1]= 2.10
mi_tupla.insert(2, "amarillo")
print(mi_tupla)
mi_tupla=tuple(mi_tupla) #la volvermos a convertir en tupla
print(type(mi_tupla))


#la tuplas si se pueden deletear pero da error
#del mi_tupla
#del mi_tupla [2] 
#print(mi_tupla) NameError= name 'mi_tupla' is not defined
# TypeError: 'tuple' object doesn't support item deletion