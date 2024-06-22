###### EXPRESIONES REGULARES #####

"""
Busca en un string 
Hay que importar la libreria re    
"""
import re 

print()
###  MATCH #### busca si hay coincidencia deesde el princio del string
txt1= "esta es la leccion numero 7: expresiones regulares"
txt2= "esta no es la leccion leccion lección numero 6: manejo de ficheros"
re.match ("esta es la leccion", txt1)   # Try to apply the pattern at the start of the string, returning a Match object, or None if no match was found.
print (re.match ("esta es la leccion", txt1, re.I)) # el re.I es para que le de igual las mayus y las minus
print (re.match ("esta es la leccion", txt2))
print (re.match ("expresiones regulares", txt1))

#lo guardo en una variable
semejanza1 = re.match ("esta es la leccion", txt1)

print (semejanza1.span()) #nos da el rango
rango0,  rango1 = semejanza1.span()
print (txt1 [rango0 : rango1])

# si no ponemos un if nos da un error AttributeError: 'NoneType' object has no attribute 'span'
 
semejanza2 = re.match ("esta es la leccion", txt2)

if semejanza2 != None:
    print (semejanza2.span()) #nos da el rango
    rango0,  rango1 = semejanza2.span()
    print (txt2 [rango0 : rango1])

semejanza2 = re.match ("esta no es la leccion", txt2)

if semejanza2 != None:
    print (semejanza2.span()) #nos da el rango
    rango0,  rango1 = semejanza2.span()
    print (txt2 [rango0 : rango1])

#ahora no hace nada pero no crashea el programa porque cundo la semejanza no se encuentra y sa un None no se mete por el if y por tanto no hace nada

print()
####### SEARCH ###### busca si hay coincidencia en algun punto sea cual sea la altuda de string en el que lo encuentr

busqueda= re.search ("leccion", txt1, re.I)
print(busqueda)

rango0,  rango1 = busqueda.span ()
print(txt1[rango0 : rango1])

print()
####### FINDALL ###### nos da un listado con las veces que lo ha encontrado

coincidencia= re.findall ("leccion", txt1, re.I)
print(coincidencia)

coincidencia= re.findall ("leccion", txt2, re.I)
print(coincidencia)

print()
####### SPLIT ###### Nos crea una lista con las secciones que divide en funcion de lo que nosotros le digamos

particion= re.split (":", txt1, re.I)
particion2= re.split (":", txt2, re.I)

print (particion)
print (particion2)

print()
####### SUB ###### para sustituir expresiones de strin

cambio = re.sub ("leccion" ,"lección",  txt1)
print(cambio)
cambio2 = re.sub ("esta es la leccion ","ESTA ES LA LECCION EN MAYUSCULAS " , txt1)
print(cambio2)
cambio3 = re.sub ("lecci[o|ó]n","LECCION  " , txt2)
print(cambio3)


### PATRONES ##### podemos crear un patron de busqueda de expresiones regulares que se pueda crear en cualquier lenguaje de programación 

#hay una tabla donde estan todas las que hay
print()

patron= r"lecci[o|ó]n"
print (re.findall (patron, txt1))
print (re.findall (patron, txt2))

patron2= r"lecci[o|ó]n | expresiones"
print (re.findall (patron2, txt1))
print (re.findall (patron2, txt2))

patron3= r"[0-7]"
print (re.findall (patron3, txt1))
print (re.findall (patron3, txt2))
print (re.match (patron3, txt1))
print (re.match (patron3, txt2))
print (re.search (patron3, txt1))
print (re.search (patron3, txt2))

patron4= r"\d" #solo busca caracteres numericos
print (re.findall (patron4, txt1))
print (re.findall (patron4, txt2))

patron5= r"\D" # solo busca caracteres no numericos
print (re.findall (patron5, txt1))
print (re.findall (patron5, txt2))

patron6= r"[l]." 
print (re.findall (patron6, txt1))
print (re.findall (patron6, txt2))

patron7= r"[l].*"
print (re.findall (patron7, txt1))
print (re.findall (patron7, txt2))

#busqueda de email por ejemplo
print()
email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$" # ^inicio del string  \.tiene en cuenta lo de detras del . y escapa despues $ final del string
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email)) 

email = "mouredev@mouredev"
print(re.findall(pattern, email))

#la mejor pagina web para aprender expresiones regulares es regex101.com