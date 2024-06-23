##### LOOPS o bucles ######
"""
mecanismo para intentar repetir algo , pasa el mismo codigo varias veces
"""
print()
print(" while")

# while
"""
hace que se repita un codigo en funcion de una condición. Al while siempre hay que pasarle un condicional
""" 
mi_condicion= 0

while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 1 #aumenta en +1 mi variable, si no le pongo esto, entraremos en un bucle infinito

print()
print(" while con else")

# while con else

while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 1 #aumenta en +1 mi variable, si no le pongo esto, entraremos en un bucle infinito
else :
    print("mi condicion es mayor que diez y se detiene el bucle  gracias al else")
    #else es opcional, el bucle si esta bien programado se debe detener solo

print()
print(" while + if y breaK")

while mi_condicion < 20:
    
    if mi_condicion == 16:
        print("mi condicion es 16 y se detiene la ejecucion ")
        break
    
    print(mi_condicion)
    mi_condicion += 1

## for  ### 
"""
hace que se repita el codigo en funcion de una condicion y se va a repetir tantas veces como elemntos haya en la lista
"""
print()
print(" for ")

mi_lista= [35,11,59,80,12,47,63]
mi_tupla=(35,1.80,"Manu", "Castilla")
mi_set= {"Manu", "Castilla", 37}
mi_diccionario= {"Nombre": "Brais", "Apellido": "Castilla", "Edad": 37}

for elemetos in mi_lista:
    print(elemetos)

for elemetos in mi_tupla:
    print(elemetos)
    
for elemetos in mi_set:
    print(elemetos)

for elemetos in mi_diccionario:
    print(elemetos)

for elemetos in list (mi_diccionario.values()):
    print(elemetos)

print()
print(" for con else if y break ")

for elemetos in mi_diccionario:
    print(elemetos)
else: 
    print("el bucle ha finalizado") 

print ()
    
for elemetos in mi_diccionario:
    print(elemetos)
    if elemetos == "Apellido":
        break
print("el programa se termina aqui")


