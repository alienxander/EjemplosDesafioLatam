import random
import sys

buscar = int(sys.argv[1])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

random.shuffle(lista)

print(f"la lista mezclada es: {lista}")

for pos, elemento in enumerate(lista):
    if elemento == buscar:
        print(f"Elemento {elemento} encontrado en la posición {pos}")
        break
    else:
        print("Elemento no encontrado")

print("Fin programa")