from sys import argv
#import getpass
from getpass import getpass
from platform import system as syspl
from os import system as sysos
#print(argv)
print('2'.isnumeric())
print('2 3'.isnumeric())
print('2'.isdigit())
print('2 3 4'.isdigit())
print(syspl())
##sysos("cls")
password2 = getpass("Ingrese una  password: ")

print(password2)
if len(argv) > 2:
    print("Demaciados parámetros")
elif len(argv) < 2:
    print("Ingrese un parámetro válido  no ha ingresado parámetros")
else:
    password = argv[1]
    if len(password) >= 6:
        print("Password correcta")
    else:
        print("Password incorrecta")
    