#######  FUNCIONES DE ORDEN SUPERIOR ############

"""
funciones dentro de otras funciones 
funciones anidadas 
existen prefabricadas dentro del sistema de python
"""

def suma1 (num):
    return num + 1 

def suma5 (num):
    return num + 5 

def sumaespecial (num1, num2, f):
    return f(num1 + num2)

print (sumaespecial(3,4,suma1))
print (sumaespecial(3,4,suma5))

print()
print()
#### closures ####
"""
son funciones que me devulven otras funciones. Dentro de una funcion 
se define otra.
"""

def sum10 (num):
    def add (valor):
        return valor + 10 + num
    return add

print (sum10 (5)(2))   

print()
print()
### funciones de orden superior que ya existen en el propio lenguaje " built - in" ###

numeros= [2,5,10,21,30]

#MAP (fx, iterable) 
"""
a partir de una lista iterable retorna otra lista iterable modificada segun una funcion
"""
#defino una funcion
def pordos(num):
    return num * 2

map (pordos, numeros)

print (list(map (pordos, numeros)))
#otra forma de hacerlo es con una lambda en vez de tener que definir la fx
print (list(map (lambda num: num *2 , numeros)))

print()
print()

# FILTER (fx , iterable)
"""
a partir de una lista iterable retorna otra lista iterable cuando se cimple una funcion por cada iterable
"""
def filtro (numero):
    if numero > 6:
        return True
    return False

filter (filtro , numeros)
print (list(filter(filtro,numeros)))
print (list(filter(lambda numero: numero > 10 ,numeros)))

print()

#REDUCE (FX , ITERABLE)
"""
Opera con un valor mas el acumulado . Este lo tenemos que importar
"""
from functools import reduce
def suma (num1 , num2):
    print (num1 , num2)
    return num1 + num2

print (reduce (suma, numeros)) # da 68 es como un sumatorio pq estamos usando suma 



