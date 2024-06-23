#### strings ###

my_string = "Mi String "
my_other_string = 'Mi other String '

print (len(my_string))
print (len(my_other_string))
print (my_string + "   " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea "
print (my_new_line_string)

my_tab_line_string = "Este es un string\tcon tabulacion de linea "
print (my_tab_line_string)

my_scape_line_string = "\tEste es un string\nescapado"
print (my_scape_line_string)

###  formateo  ###

nombre ,apellido, edad = "m" , "c" , 37
print ("mi nombre es {} {} y mi edad es {}" .format (nombre, apellido, edad))
print ("mi nombre es %s %s y mi edad es %d" %(nombre,apellido,edad))

print ("mi nombre es {nombre} {apellido} y mi edad es {edad}")#formatear e inferir datos mal
print (f"mi nombre es {nombre} {apellido} y mi edad es {edad}") #formatear e inferir datos bien

###€ desempaquetado de caracteres ####
lenguaje= "python"
a , b , c , d , e , f  = lenguaje
print (a)
print (b)
print (c)
print (d)
print (e)
print (f)
print (a,b,c,d,e,f)

lenguaje_cortado= lenguaje[0:6]
print(lenguaje_cortado)
lenguaje_cortado= lenguaje[0:3]
print(lenguaje_cortado)
lenguaje_cortado= lenguaje[3:6]
print(lenguaje_cortado)
lenguaje_cortado= lenguaje[0:5]
print(lenguaje_cortado)

### reversion ###

lenguaje_reverso= lenguaje[::-1]
print(lenguaje_reverso)

#### ordenas las letras en orden alfabetico SORTED ###
txt = sorted(lenguaje)
print (txt)

### funciones del sistema ###

print(lenguaje.capitalize()) #poner en mayusculas la primera letra
print(lenguaje.upper()) #poner en mayusculas todas las letras
print(lenguaje.lower()) #poner en minusculas todas las letras
print(lenguaje.upper().isupper()) #esta en mayusculas?
print(lenguaje.isupper()) #esta en mayusculas?
print(lenguaje.count("t")) #contar cuantas t tiene
print(lenguaje.isnumeric ()) #es un numero? boleana true o false
print("2".isnumeric()) #es un numero? boleana true o false
print(lenguaje.startswith ("py")) #empieza por "" boleana true o false
print(lenguaje.startswith ("py")) #empieza por ""? boleana true o false
print(lenguaje.startswith ("m")) #empieza por ""? boleana true o false