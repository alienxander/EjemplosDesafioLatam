from os import system as sysos
from platform import system as syspl

def limpiar_consola():
    if syspl() == "Windows":
        sysos("cls")
    elif syspl() == "Linux":
        sysos("clear")