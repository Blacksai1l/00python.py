#####listas comprensivas ####
"""
es un formato concreto para crear listas, son lista que se hacen a partir de otra lista 
"""
mi_lista_original = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(mi_lista_original)

mi_lista_comprimida = [i for i in range (8)]
print(mi_lista_comprimida) 

mi_rango = range (8)
print (list(mi_rango))

mi_lista_comprimida = [i * i for i in range (8)]
print(mi_lista_comprimida) 

def suma_cinco (num):
    return num + 5

mi_lista_comprimida = [suma_cinco(i) for i in range (8)]
print(mi_lista_comprimida) 
