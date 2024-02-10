#Concatenación
print("Hola " + "mundo!!")
print("Hola " + "mundo " + str(2))
print("Mi cadena" + str(True))
#Duplicar un texto
print("Hola " * 3)
###Hola Hola Hola
#Métodos
##Count: Cuenta las ocurrencias de un caracter en una cadena de carácteres
print("Ejemplo de metodo count: ".count("o"))
print("Ejemplo de metodo count emp: ".count("emp"))
print("Ejemplo de metodo count (o): " + str("Ejemplo de metodo count".count("o")))

"""
Comentarios de 
varias
líneas
"""

##upper: transforma toda la cadena de caracteres en mayúscula
print("hola mundo".upper())

##lower: transforma el texto en minúsculas
print("HOLA MUNDO".lower())

##title: Tranforma a mayúscula la primera letra e cada palabra
print("hola mundo!!!".title())

##len o __len__: cuenta los carácteres de un string
print("hola mundo".__len__())
print("hola mundo 2".__len__())
print(len("hola mundo 2"))

##split: Separa una cadena de carácteres
print("Manzana Pera Frutilla Mandarina Naranja".split())
print("Manzana,Pera,Frutilla,Mandarina,Naranja".split(","))
print("Manzana,Pera,Frutilla,Mandarina,Naranja".split(",", 3))
print("Manzana,Pera,Frutilla,Mandarina,Naranja".split(",")[3].count("a"))

##join: Une los elementos de un objeto iterable

print(" y ".join(['Manzana', 'Pera', 'Frutilla', 'Mandarina', 'Naranja']))

##Salto de linea en string
"""
Hola
a
todos

El salto de línea se hace con \n
"""

print("\"Hola mundo con comillas!!\"")
print("\"Hola \nmundo\ncon\ncomillas!!\"")

##VARIABLES
"""
    Reglas de las variables: 
        snake_case: variable_uno
        -> No puede tener espacios y no deben comenzar con un número
        -> la primera letra debe ser minúscula --> todo en minúscula
        -> debe ser auto explicativa --> variable_uno(mal) --> resultado_suma (Bien)
    
        resultado_1 (bien)
        resultado1 (bien)
        1_resultado (mal)
    Numéricas
        enteros
        decimales --> float
    Booleanas
        True o False
    Texto o string: Cadena de carácteres
"""
mi_entero = 12
mi_entero2: int = 23
print("Mi entero: " + str(mi_entero))
mi_entero = 12.1
print("Mi entero decimal: " + str(mi_entero))
mi_entero = "12.1"
print("Tipo de mi entero: " + str(type(mi_entero)))
print(type(mi_entero))
mi_entero = 1

if type(mi_entero) is str:
    print("Mi entero es un string")
else:
    print("Mi entero no es un string")

print("Mi entero decimal: " + str(mi_entero))
mi_float = 1.9
mi_string = "Mi string"
mi_string = 'Mi string'
mi_booleano = True
mi_booleano = False
mi_booleano2: str
mi_str2: str = "Hola mundo"
mi_bool2: bool
mi_float2: float
mi_int2: int
mi_str2 = 3
print(mi_str2)
print(type(mi_str2))

#Interpolación
nombre:str = "Alienxander"
apellido:str = "Beck"

print("El nombre completo es {} {}".format(nombre, apellido))
print("El nombre completo es" + nombre + " " + apellido)
print("El nombre completo es {{{} {}}}".format(nombre, apellido))
print("El nombre completo es {}{} {}{}".format("{", nombre, apellido, "}"))

#Precisión de los datos --> float
numero1: int = 1
numero2: int = 9
resultado_div = numero1 / numero2

print(f"El resultado de la división es {resultado_div}")
print(f"El resultado es {resultado_div:.2f}")
print(f"El resultado es {resultado_div:.3f}")

##input: entrada de datos
nombre = input("Ingrese Nombre: ")
print(type(nombre))
print(type(bool(nombre)))
print("El nombre ingresado es: " + nombre)
print(''' esto es un parrafo 
      nuevo y 
      mas nuevo''')

