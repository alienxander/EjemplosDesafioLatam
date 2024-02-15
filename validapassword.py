from sys import argv
#import getpass
from getpass import getpass
#print(argv)
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
    