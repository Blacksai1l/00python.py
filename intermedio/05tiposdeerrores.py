#### TIPOS DE ERRORES ####

"""
VAMOS A IR VIENDO Y REPASANDO TODAS LAS EXECPCIONES QUE PUEDE LANZAR PYTHON Y VAMO S A IR VIENDO 
COMO RECREEAR EL ERROR Y LO QUE APARECE EN CONSOLA. 
NO HAY CODIGO SIN ERROR
"""

#SYNTAXERROR

#print "Hola comunidad" # error de sintaxis => SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print ("Hola comunidad")

#NAMEERROR

#print(variable) # la variable no esta definida~
variable= "variable random"
print (variable)

#INDEXERROR

miLista= ["python", "Swift", "Kotlin", "Rust", "PineScript", "JavaScript"]
print (miLista[0])
print (miLista[1])
print (miLista[2])
print (miLista[3]) #imprime el elemeto en en la posicion 3 empezando desde el 0 , es decir lo que está en 4ta posicion
print (miLista[4])
print (miLista[5])
print (miLista[-1]) # empieza por el final
# print (miLista[6]) #IndexError: list index out of range

#MODULENOTFOUNDERROR

# import maths #ModuleNotFoundError: No module named 'maths'
import math

#ATRIBUTEERROR

#print(math.PI) # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)

#KEYERROR
#recuerda: los diccionarios son estructuras que nos permite guardar información en una clave, el diccionario no es una estructura ordenada es decir que no puedo imprimir accediendo a la posicion como hacemos con las listas sino que tenemos que imprimar accediendo a la palabra clave

miDiccionario= {"Nombre": "Manu" , "Apellido":"Castilla", "Edad" : 37 , "Altura" :1.81 , 1 :"Python"}
print(miDiccionario["Nombre"])
print(miDiccionario[1])
#print(miDiccionario["APELLIDO"]) #KeyError: 'APELLIDO'
print(miDiccionario["Apellido"])

#TYPEERROR

#print(miLista["0"]) #TypeError: list indices must be integers or slices, not str
print(miLista[0]) 

#IMPORTERROR

#from math import PI #ImportError: cannot import name 'PI' from 'math' (unknown location). Did you mean: 'pi'?
from math import pi
print(pi)

#VALUERROR 
miEntero= int("10")
#mi2Entero= int ("10 años") #ValueError: invalid literal for int() with base 10: '10 años'
print(type("10"))
print(type(miEntero))
print(type("10 años"))

#ZERODIVISIONERROR

print(4/2)
#print(4/0) #ZeroDivisionError: division by zero