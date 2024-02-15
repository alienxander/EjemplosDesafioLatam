from sys import argv


#print(argv)
# numero = int(input("Ingrese un número: "))

if argv[1].isdigit():
    numero = int(argv[1])

    if numero < 0:
        print("Debe ingresar un número mayor o igual a cero")
    elif numero == 0: 
        print("Ha ingresado un cero")
    elif (numero % 2) == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")
else:
    print("Ingrese un valor numérico!!!")

# if numero >= 0:
#     if numero == 0: 
#         print("Ha ingresado un cero")
#     elif (numero % 2) == 0:
#         print(f"El número {numero} es par")
#     else:
#         print(f"El número {numero} es impar")
# else:
#     print("Debe ingresar un número mayor o igual a cero")

