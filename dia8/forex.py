
# it_object = ["Pera", "Manzana", "Fritilla"]

# for fruta in it_object:
#     print(f"Fruta: {fruta}")

# it_object = [
#     {'id': 1, 'descripcion': 'Pera'}, 
#     {'id': 2, 'descripcion': 'Manzana'}, 
#     {'id': 3, 'descripcion': 'Frutilla'}
# ]

# for fruta in it_object:
#     print(f"Fruta: id: {fruta.get('id')} - {fruta.get('descripcion')}")

# print(range(10)) # Desde 0 - 9
# print(range(2, 10)) # 2 - 9
# print(range(2, 20, 3)) # 2 - 17 de 3 en 3
# print("****************************\n")
# for i in range(10):
#     print(i)
# print("****************************\n")
# for i in range(2, 10):
#     print(i)

# print("****************************\n")
# for i in range(2, 21, 3):
#     print(i)

# print("****************************\n")
# for i in range(10, 21, 2):
#     print(i)

# print("****************************\n")
# for i in range(10, 21):
#     print(i)
    
texto = "hola mundo"
for caracter in texto:
    print(caracter)

# hola mundo
# hola
# ... 10 veces
#............ (Ok)

mi_dicc = {
    'nombre': 'Alexander',
    'apellido': 'Beck',
    'edad': 39,
    'hijos': [
        {'nombre': 'Oliver', 'apellido': 'Beck', 'edad': 7, 'juega_futball': False},
        {'nombre': 'Mila', 'apellido': 'Beck', 'edad': 10, 'juega_futball': True}
    ]
}

for clave, valor in mi_dicc.items():
    #print(type(valor))
    if type(valor) == list:
        for pos, elemento_lista in enumerate(valor):
            print(f"Hijo {pos + 1} .... {elemento_lista}")
    else:
        print(f"Mi clave {clave} = {valor}")

mi_dicc.update({'nombre': 'otro'})

print(mi_dicc)

texto = "Hola Mundo"

for pos, caracter in enumerate(texto):
    print(f"{pos}: {caracter}")

lista_hijos = ['Oliver', 'Mila', 'Otro']
lista_edades = [7, 9, 10]
lista_juegos = ['Futball', 'Basquet', 'Otro juego']

# for hijo, edad, juego in zip(lista_hijos, lista_edades, lista_juegos):
#     if hijo == 'Mila':
#         break
#     else:
#         print(f'{hijo} tiene {edad} años y le gusta jugar {juego}')

for hijo, edad, juego in zip(lista_hijos, lista_edades, lista_juegos):
    print(f'{hijo} tiene {edad} años y le gusta jugar {juego}')
    
list1 = [1, 2, 3, 4]
list2 = [5, 6]
print("**************---******************")
for element_list_1 in list1:
    for element_list_2 in list2:
        print(f"Elementos ({element_list_1}, {element_list_2})")

        





    






