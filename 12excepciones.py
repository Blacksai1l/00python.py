### manejo de errores ####
"""
de alguna forma permitir que el programa siga funcionando y que no se cierre 
aunque tengamos un error 
"""
num1 , num2 = 5 , 1

if type(num1) and type(num2) == int :
    print  ( num1 + num2)
else:
    print ("no se cumplió")
print()
print("el programa sigue ejecutandose")
#ahora vamor a definir uno de los numeros como un texto y debe de dar error 

num1 , num2 = 5 , "1"

if type(num1) and type(num2) == int :
    print  ( num1 + num2)
else:
    print ("no se cumplió")
print()
print("el programa sigue ejecutandose")
###ahora vamos a ver el try y el except

try:
    print(num1 + num2)
    print("no se ha producido un error")
except:
    print("se ha producido un error")

print()
print("el programa sigue ejecutandose")

### try except y else

try:
    print(num1 + num2)
    print("no se ha producido un error")
except:
    #se ejecuta si se ha producido un error
    print("se ha producido un error")
else: 
    #se ejecuta si no se ha producido una excepcion
    print("el programa sigue ejecutandose")

### try except , else , finally

try:
    print(num1 + num2)
    print("no se ha producido un error")
except:
    #se ejecuta si se ha producido un error
    print("se ha producido un error")
else: 
    #se ejecuta si no se ha producido una excepcion
    print("el programa sigue ejecutandose")
finally:
    #se ejecuta siempre 
    print("sigue le ejecución")

print ()
print ()
# excepciones por tipo si queremos capturar errores muy concretos

try:
    print(num1 + num2)
    print("no se ha producido un error")
except TypeError:
    print("se ha producido un error TypeError")
except ValueError:
    print("se ha producido un error ValueError")

print ()
print ()

#si ademas queremos que el programa no pete pero si nos diga el tipo de error que hemos tenido 
#lo podemos guardar en una variable mi_error
try:
    print(num1 + num2)
    print("no se ha producido un error")
except TypeError as mi_error:
    print(mi_error)
except ValueError as mi_error1:
    print(mi_error1)
except Exception as mi_error2:
    print(mi_error2)