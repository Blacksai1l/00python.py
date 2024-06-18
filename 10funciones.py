####### FUNCIONES ######
"""
una funcion va a intentar dar solucion a un problema
muy concreto que tengamos
Todo el codigo que va a solucionar un problema
va a estar bajo la funcion  y por tanto se evitan 
errores por duplicidad. 
Se usa la palabra def para definirlas. 
Se la define y despues se la llama para que ejecute el codigo 
o para que nos muestre el codigo
"""
print ()
def mi_funcion (): 
    print("esto es una función")

mi_funcion()
mi_funcion()
mi_funcion()

#definimos una funcion de suma 

print ()

def sumatorio (primer_numero, segundo_numero ):
    print (primer_numero + segundo_numero)

sumatorio (5, 10)
sumatorio (25, 8004510)
sumatorio (5456866, 1066454)
sumatorio (545686.56, 106.4)

#la funcion ademas de recibir parametros tbn los puede retornar

print ()

def sumatorio_con_retorno (primer_numero, segundo_numero):
    return primer_numero + segundo_numero
#el resultado de la funcion hay que asignarlo a una variable
#o guardarlo a una variable
mi_resultado= sumatorio_con_retorno(5,10)
print (mi_resultado)

print ()

def nombre (Nombre, Apellido):
    print(f"{Nombre} {Apellido}") # f" para dar formato una cadena de texto

nombre ("Manu", "Castilla")

def nombre (Nombre, Apellido, Alias= "sin alias"):# al alias le digo que por defecto ponga sin alias
    print(f"{Nombre} {Apellido} {Alias}") # f" para dar formato una cadena de texto

nombre ("Manu", "Castilla")
nombre ("Manu", "Castilla", "Mojonario")

print()

def impresora_de_texto (*texto): #el * hace que le pueda pasar varias parametros 
    print(texto)

impresora_de_texto ("ola", "que", "ase")
impresora_de_texto ("manue")

#otra forma de hacerlo ademas añadiendo mayusculas

def impresora_de_texto (*textos): #el * hace que le pueda pasar varias parametros 
    for text in textos:
        print(text.upper())
        

impresora_de_texto ("ola", "que", "ase")
impresora_de_texto ("manue")

#ahora vamos a pedirle al usuario que meta los parametros de la funcion
print()
print("Este programa sirve para sumar dos números")

x= input ("¿cual es el primer numero que quieres sumar? ") 
y= input("¿cual es el segundo numero que quieres sumar ? ")

def suma (x,y):
   print (x + y)

suma (x , y)