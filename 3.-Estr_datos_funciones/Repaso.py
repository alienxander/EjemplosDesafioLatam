from sys import argv

lista = [1, 2, 3, 4]

len(lista)

for item in lista:
    print(item)
    
lista_alumnos = [
    {
        "nombre": "Carlos",
        "nota": 7
    },
    {
        "nombre": "Otro",
        "nota": 7
    },
    {
        "nombre": "Pepito",
        "nota": 6
    }
]

dicc_nota = {
            "nombre": "Carlos",
            "nota": 7
        }


# dicc_nota["nota"] = 6

# print(dicc_nota)

lista_castigo = [alumno for alumno in lista_alumnos if alumno["nota"] == 7]
lista_resultante = []
for castigado in lista_castigo:
    castigado["nota"] -= 0.5
    lista_resultante.append(castigado)

print("Castigados: ", lista_resultante)

pais = ['Manzana', 'Pera', 'Frutilla']
calibre = [10, 5, 6]

print(zip(pais, calibre))

for k, v in zip(pais, calibre):
    print(k, v) 
    
dicc_calibres = [{k:(v + 1)} for k, v in zip(pais, calibre)]   

print(dicc_calibres)

lista_numeros:list = [1, 2, 3, 4, 5]

print(lista_numeros[-1], lista_numeros[-2], lista_numeros[-3], lista_numeros[-4], lista_numeros[-5])
print(lista_numeros[4], lista_numeros[3], lista_numeros[2], lista_numeros[1], lista_numeros[0])

print(lista_numeros[:3])
#print(lista_numeros[6])
print(lista_numeros[1:6])

print(argv)
