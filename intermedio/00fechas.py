### fechas ###


# importamos el modulo de python de fecha (datetime)

from datetime import datetime

now= datetime.now() # ahora creamos una variable para llamar una funcion de datetime CON LA FECHA DE AHORA

print (now)
print (now.day)
print (now.month)
print (now.year)
print (now.hour)
print (now.minute)
print (now.second)
print (now.timestamp ())


print ()
print ()
# ahora vamos a crear otra varible con la  fecha que represente el comienzo del nuevo año 

año24 = datetime(2024 , 1 , 1 , 15) # tanto tiempo como fecha

def print_date (fecha):
    print (fecha)
    print (fecha.day)
    print (fecha.month)
    print (fecha.year)
    print (fecha.hour)
    print (fecha.minute)
    print (fecha.second)
    print (fecha.timestamp ())

print_date (año24)

print ()
print ()


# ahora importamos de datetime otra varaiable que es tiempo  ( time)

from datetime import time #solo tiempo sin fecha

# ahora creamos la variable para llamar a la funcion
ahora_mismo = time(18, 11 , 20)

print (ahora_mismo.hour)
print (ahora_mismo.minute)
print (ahora_mismo.second)

ahora_mismo = time (18, 11 , 20)

print (ahora_mismo.hour)
print (ahora_mismo.minute)
print (ahora_mismo.second)

print()

from datetime import date # solo fecha sin timepo

fecha_actual= date (24 , 6, 10 )

print (fecha_actual.year)
print (fecha_actual.month)
print (fecha_actual.day)

print ()
fecha_actual= date.today ()
print (fecha_actual)
print (fecha_actual.year)
print (fecha_actual.month)
print (fecha_actual.day)

print ()

#podemos hacer operaciones con las fechas también fechas con fechas , timepo con tiempo ... etc

mes_anterior= date(fecha_actual.year, fecha_actual.month-1, fecha_actual.day)

print(mes_anterior)


diferencia= fecha_actual - mes_anterior
print (diferencia)

print()

from datetime import timedelta

cero_timedelta = timedelta(200,10,100,weeks=10)
final_timdelta = timedelta(300,10,100,weeks=12)

print (final_timdelta - cero_timedelta)
print (final_timdelta + cero_timedelta)

