### LAMBDAS ###

"""
entendemos que las lambdas son como funciones pero con la peculiaridad que son
funciones anonimas, es decir que no tiene nombre. Cuando definiamos una funcion 
siempre le teniamos que poner un nombnre 
def nombre ():

Ahora no hace falta nombre 

una lamba tiene tambien la peculiaridad que la podemos almacenar en una variable
esto es una manera de simplicar funciones
"""

lambda primer_valor , segundo_valor: primer_valor + segundo_valor

# la guardo en una variable 

variable_suma= lambda primer_valor , segundo_valor: primer_valor + segundo_valor

print (variable_suma( 2 , 4))

variable_multi = lambda primer_valor , segundo_valor: primer_valor * segundo_valor 

print (variable_multi (2 , 3) )

# puede haber lambdas dentro de funciones 

def sumadetres (x1):
    return lambda valor1 , valor2, : valor1 + valor2 + x1

print (sumadetres (5)(2 , 2))

