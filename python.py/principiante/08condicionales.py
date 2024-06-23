#### condicionales ####


micondicion = True

if micondicion: # busca si es True
    print ("se ejecuta la condicion del if")

print ("La ejecición continua ")


micondicion = False

if micondicion:
    print ("se ejecuta la condicion del if") # en este caso no se imprime porque busca si el true y mi variable es false




print ()
print ()
print ("La ejecición continua ")
print ()

micondicion= 5*2

if micondicion:
    print ("se ejecuta la condicion del primer if")

if micondicion == 11 : 
    print("se ejecuta la condicion del segundo if")

if micondicion == 10 : 
    print("se ejecuta la condicion del tercer if")

if micondicion >= 10 : 
    print("se ejecuta la condicion del cuarto if")

if micondicion <= 10 : 
    print("se ejecuta la condicion del quinto if")


if micondicion < 10 : 
    print("se ejecuta la condicion del sexto if")

if micondicion < 10 : 
    print("se ejecuta la condicion del septimo if")

print ()
print ()
print ("La ejecición continua ")
print ()

## if y else 

if micondicion > 10:
    print ("Es mayor que 10")
else: 
    print("Es menor o igual a 10")

if micondicion < 10:
    print ("Es menor que 10")
else: 
    print("Es mayor o igual a 10")

### podemos tener mas de una condicion 

if micondicion > 10 and micondicion< 20:
    print ("Es mayor que 10 y menor de 20 ")
else: 
    print("Es menor o igual a 10 o mayor que 20")

if micondicion < 10 and micondicion < 20 :
    print ("Es menor que 10 y menor que 20 ")
else: 
    print("Es mayor o igual a 10 y menor que 20")

print ()
print ()
print ("La ejecición continua ")
print ()

###elif  es una comrpobacion extra 

if micondicion < 10 and micondicion < 20 :
    print ("Es menor que 10 y menor que 20 ")
elif micondicion ==10 :
    print ("la condicion es igual a 10 # se vas por el elif")
else: 
    print("Es mayor o igual a 10 y menor que 20")

if micondicion < 10 and micondicion < 20 :
    print ("Es menor que 10 y menor que 20 ")
elif micondicion ==1 :
    print ("la condicion es igual a 1")
else: 
    print("Es mayor o igual a 10 y menor que 20 # no se va por el elif entonces escoge el else")

print ()
print ()
print ("La ejecición continua ")
print ()

mistring= ""

if mistring :
    print ("se pinta si mi cadena de texto es True al estar vacia es False por lo que no se imprime")

if not mistring:
    print ("mi cadena de texto esta vacia")

mistring= "mi cadena de texto"

if mistring :
    print ("mi cadena de texto no esta vacia # ahora si se imprime porque es True")

print ()
print ()
print ("La ejecición se terminó ")
print ()