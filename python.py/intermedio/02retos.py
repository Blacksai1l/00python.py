#### retos de codigo ####

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

"""
def fizzbuzz ():
    for indice in range (1,101):
        if indice % 3 == 0 and indice % 5 == 0:
            print("fizzbuzz")
        elif indice % 3 == 0:
            print ("fizz")
        elif indice % 5 == 0:
            print ("buzz")
        else:
            print (indice)

fizzbuzz()

print()
print()
print()
"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def es_anagrama (txt1 , txt2):
    if txt1.lower () == txt2.lower():
        return False  #para que no detecte como anagrama la misma palabra  
    return sorted(txt1.lower()) == sorted (txt2.lower ()) # sorted retorna una nueva lista con todo los elementos y los ordena 

print (es_anagrama("amor" , "Roma"))
print (es_anagrama("amor" , "lola"))
print (es_anagrama("Cosa" , "asco"))



print()
print()
print()
"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibo ():
    
    numprevio = 0
    numposterior = 1
    
    for indice in range (1 ,51):
        
        print (numprevio)

        fibonacci = numprevio + numposterior
        numprevio = numposterior
        numposterior = fibonacci 
        
fibo ()



print()
print()
print()
"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def esPrimo (numero):
    if numero <=1:
        print (numero, "no es primo") 
    
    elif numero== 2:
        print (numero, "es primo")

    else:
        for x in range (2 , numero):
            if numero % x == 0: 
                print (numero, "no es primo")
                return False
            print (numero, "es primo")
            return True
   
        
esPrimo(1)
esPrimo(2)
esPrimo(3)
esPrimo(4)
esPrimo(5)
esPrimo(6)
esPrimo(7) 


print ()

def impresoraPrimosdel1al100 ():
    for num in range (1 , 101):
        if num >= 2:
            
            es_divisible= False
            
            for n in range (2, num):
                
                if num % n == 0 :
                    es_divisible= True
                    break 
                
            if not es_divisible:
                print (num)
        
impresoraPrimosdel1al100()

print()
print()
print()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
mi_string= "Hola mundo"
mi_string_invertida= mi_string [::-1]

print(mi_string)
print (mi_string_invertida)

# la forma de hacerlo manulmente es asi

def invertir(text):
    lenText= len(text) # me dice la longitud del texto en este caso hola 4
    text_invertida= "" # aqui voy a ir guardando lo que me va devolviendo el for
    for n in range (0 , lenText):
        text_invertida += text [lenText - n -1] #aqui voy asignando cada letra de mi  nuevo texto invertido
    print (text_invertida)
    return text_invertida
    
invertir ("hola")


