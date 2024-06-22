#### MANEJO DE FICHEROS #####



### TXT FILES  ### 
import os

#miFichero = open ("intermedio/miFichero.txt" , "w") #w modo escritura
#miFichero = open ("intermedio/miFichero.txt" , "r") #r modo lectura 
miFichero = open ("intermedio/miFichero.txt" , "w+") # r+ leer y escribir
#miFichero = open ("intermedio/miFichero.txt" , "w+") #w+ modo escritura/lectura y lo sobreescribe
#print(miFichero.read())
#print(miFichero.write ("HolaMadafaka") ) 
#print(miFichero.read(10))
#print(miFichero.readline())
#print(miFichero.readline())
#print(miFichero.readlines())

# lo tenemos abierto y con los siguientes lineas y gracias al w+ lo vamos a reescribir

miFichero.write ("\nMi nombre es Manolete")
miFichero.write ("\nMi apellido es Torete")
miFichero.write ("\ntengo 37 años")
miFichero.write ("\nmi lenguaje favorito es Python")
miFichero.write ("\ntambien me gustaria aprender Rust")

miFichero.close() #para cerrar el fichero

with open ("intermedio/miFichero.txt") as miOtroFichero:
    for line in miOtroFichero.readlines():
        print(line)

miFichero.close()
miOtroFichero.close()


#os.remove ("intermedio/miFichero.txt") #para borrar el fichero

### JSON FILES  ### 
"""
son ficheros en formato de diccionario con item --> valor
"""
import json

miFicheroJson= open ("intermedio/miFicheroJson.json" , "w+")

jsontest= {
    "name": "Manolete",
    "surname": "Toreto",
    "age": 37,
    "languajes": ["Python", "Rust", "C++", "JavaScript"],
    "team": "Betis" }

json.dump (jsontest, miFicheroJson, indent= 2) # .duimp sirve para escribir el fichero json- indent es el espacio que dejamos a la izquierda del texto.

miFicheroJson.close() #para cerrar el fichero

with open ("intermedio/miFicheroJson.json") as miOtroFicheroJson:
    for line in miOtroFicheroJson.readlines():
        print(line)

miFicheroJson.close()
miOtroFicheroJson.close()

diccionarioJSON= json.load (open("intermedio/miFicheroJson.json"))
print (diccionarioJSON)
print (type(diccionarioJSON))
print(diccionarioJSON["name"])


##### CSV #####
import csv
micsv = open ("intermedio/micsv.csv" , "w+")

miOtroCSV= csv.writer(micsv)
miOtroCSV.writerow (["name","surname","age","languajes","team" ])
miOtroCSV.writerow (["Manolete","Toreto",37,"Python","Betis" ])
miOtroCSV.writerow (["Antoñete","Pedrin",23,"Rust","Betis" ])
miOtroCSV.writerow (["Juanele","Sarmiento",30,"Python","Sevilla" ])

micsv.close ()

with open ("intermedio/micsv.csv") as miOtroFicheroCSV:
    for line in miOtroFicheroCSV.readlines():
        print(line)




##### XLSX #####
#import xldr #deme instalarse el modulo que no está precargado en python





##### XML #####
import xml