#### modulos ####

#vamos a crear un fichero donde vamos a definir varias funciones y despues las podemos importar

import funciones_de_modulo

funciones_de_modulo.suma (6 , 1)
funciones_de_modulo.resta (6 , 1)
funciones_de_modulo.multiplicacion (6 , 1)



#otra forma es llamar solo a una funcion asi nos ahorramos el funcionesdemodulo.----

from funciones_de_modulo import suma , resta

suma (9 , 10)
resta (10 , 9)


# python tiene modulos predeterminados que podemos usar 

import math

print (math.log (10 , 2))
print(math.pi)
print(math.pow(2 , 3))# dos elevado a tres por ejmeplo

#también podemos importar y renombrar una funcion 

from math import pi as elNumeroPi

print(elNumeroPi)