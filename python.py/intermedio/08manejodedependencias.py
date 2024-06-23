###### GESTOR DE PAQUETES PARA PYTHON #######
"""
una herramienta que se llama pip
pip install pip 
https://pypi.org
hay que ir instalando los paquetes desde la terminal , primero instalar el gestor de paquetes pip y despues 
los paquetes en si con pip install paquete
pip list en terminal -->> nos da la lista de paquetes que tenemos instalados con la versions

"""
# NUMPY permite hacer calculos numericos mas complejos que los que permite el paquete de python en si
#pip install numpy
import numpy 

print (numpy.version.version)

miLista = [35,25,14,17,89,56,45,1,3,8,11,66,88]
miArray = numpy.array ([35,25,14,17,89,56,45,1,3,8,11,66,88])
print(type (miLista))
print(type (miArray))
print(miLista *2) # impreme la lista 2 veces
# print(miLista / 2 ) TypeError: unsupported operand type(s) for /: 'list' and 'int'
print(miArray)
print(miArray / 2 ) # no da error
print(miArray * 2 ) # multiplica los numeros de la lista *2 y no pone la lista dos veces


#PANDAS #pip install pandas 
"""
Powerful data structures for data analysis, time series, and statistics
"""
import pandas

# REQUEST #pip install requests
#sirve para llamar a la api.
import requests

"""
respuesta =  requests.get ("https://pokeapi.co/api/v2/pokemom?limit=151!")

print (respuesta)
print (respuesta.status_code)
print (respuesta.json())

"""

# VAMOS A HACER UN PAQUETE NOSOTROS
# hay que crear un archivo con dos ficheros un llamado __init__.py lo dejamos en blanco 
# y lo guardamos y otro que se llama operacion.py donde vamos a poner lo que queremos usar.

from paquete import operaciones
print (operaciones.suma (1 , 44))