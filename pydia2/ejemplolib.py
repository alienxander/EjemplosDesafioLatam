#Librerías
import os ##Permite acceder al sistema operativo
#from os import getcwd
import math #Añade funciones matemáticas
import random
from datetime import datetime
import pytz

print("Ruta actual: ", os.getcwd())
#print("Ruta actual: ", getcwd())
print(math.sqrt(4)) #Raíz cuadrada
print(math.ceil(math.sqrt(123))) #Raíz cuadrada
print(math.factorial(3))
print(math.floor(5.6))
print(random.random())
print(random.randint(1, 5))

utcmoment_naive = datetime.utcnow()
#print("UTC pytc: ", pytz.timezone('America/Santiago'))
pytz.timezone('America/Santiago')
utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)

# print "utcmoment_naive: {0}".format(utcmoment_naive) # python 2
print("utcmoment_naive: {0}".format(utcmoment_naive))

print(datetime.now())

print("Hola Mundo!!"[5], "Hola Mundo!!"[9], "Hola Mundo!!"[5:10])

hola = "Hola Mundo!! de nuevo"

print(hola[5:len(hola)])
