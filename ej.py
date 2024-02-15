#Opciones de menú
from math import pi
CUADRILATERO = 0
CIRCULO = 1
area: int = 0
radio:int = 0

print("Menu: ")
print("0: Cuadrilátero: ")
print("1: Circulo: ")
menu = int(input("Ingrese una opción de menú: "))

#Repite mientras la condición sea verdadera
while menu != CIRCULO and menu != CUADRILATERO:
    print("Menu: ")
    print("0: Cuadrilátero: ")
    print("1: Circulo: ")
    menu = int(input("Ingrese una opción de menú: "))

if menu == CUADRILATERO:
    base = float(input("Ingrese la base para el cuadrilátero"))
    altura = float(input("Ingrese la altura para el cuadrilátero"))
    area = base * altura
    print("El área es: ", area)
    
if menu == CIRCULO:
    radio = float(input("Ingrese el radio para la circunferencia"))
    area = pi() * radio**2
    print("El área es: ", area)