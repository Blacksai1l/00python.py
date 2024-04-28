#vamos a ver las variables

mi_variable= "mi string varialble"
print (mi_variable)
mi_variable_booleana = True
print (mi_variable_booleana)



#transformar una variable entera a string 

numero= 5
strnumero = str (numero)
print(strnumero)
print (type (strnumero) )


#concatenación de variables en print

print (mi_variable, mi_variable_booleana, numero, strnumero)

#variables en una sola linea

nombre, apellido,alias, edad = "Manu", "Castilla", "Mojonario" , "36"
print (nombre,apellido, edad, alias)


#funciones del sistema con variables 

print(len (mi_variable)) # cuenta el numero de caracteres contando los espacios
print(len (strnumero))

nombre=input ("¿como te llamas? ") #input pide un valor
edad= input("¿Cual es tu edad? ")
print("tu nombre es " , nombre, "tu edad es ", edad) #print imprime