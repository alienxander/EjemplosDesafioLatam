from getpass import getpass
from os import system as sysos
from platform import system as syspl

MI_PASSWORD = "123456"

def limpiar_consola():
    if syspl() == "Windows":
        sysos("cls")
    elif syspl() == "Linux":
        sysos("clear")

def valida_password(password):
    if password == MI_PASSWORD:
        return True
    
    return False

limpiar_consola()

password = getpass("Ingrese Password: ")

while not valida_password(password):
    print("Password Incorrecta..")
    #password = getpass("Ingrese nuevamente la password: ")

# a = 3
# b = 0
# if a == 2:
#     b == 3
#     a = a + b
# else:
#     a = a + b


print("Acceso correcto")