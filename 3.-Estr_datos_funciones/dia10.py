# Concatenar o unir dos listas

lista1 = [1, 2, 3, 4]
lista2 = [5, 6]

lista_concatenada = lista1 + lista2

print(lista_concatenada)

lista_multiplicada = lista_concatenada * 3

print(lista_multiplicada)

lista_multiplicada[len(lista_multiplicada):] = [20, 30]

print(lista_multiplicada)

lista_multiplicada[5:7] = [1000, 2000]

print(lista_multiplicada)
##Inserta un elemento en la lista
lista_multiplicada.insert(5, 3000)

print(lista_multiplicada)

lista_multiplicada.remove(6)
lista_multiplicada.remove(3000)

print(lista_multiplicada)

#print(lista_multiplicada.__dir__())

print(lista_multiplicada.__contains__(2000))

lista_multiplicada.append(10000)

lista_nueva = lista_multiplicada

print(lista_multiplicada)

lista_multiplicada.pop()

print(lista_multiplicada)

#lista_multiplicada.remove(10000)

lista_multiplicada.reverse()

print(lista_multiplicada)

lista_multiplicada.sort()

print(lista_multiplicada)

lista_multiplicada.sort(reverse=True)

print(lista_multiplicada)

print(lista_multiplicada.count(2000))

print(lista_multiplicada.index(30))

lista_copia = lista_multiplicada.copy()

#lista_copia = lista_multiplicada

#lista_multiplicada = []

print("Lista_copia: ", lista_multiplicada, lista_copia)

if lista_copia == lista_multiplicada:
    print("Las listas son iguales")
    
lista_multiplicada.clear()

print(lista_multiplicada, lista_copia)

lista_multiplicada.extend([1, 2, 3])

print(lista_multiplicada)

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


print(lista_alumnos.__getitem__(0))
    




#print(lista_copia)

