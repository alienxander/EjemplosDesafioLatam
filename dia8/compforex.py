
n = 10

lista = [(2 * i) + 2 for i in range(10)]

print(lista)

lista = [0, 3, 6, 7, 8, 9]

divisible = []

divisible = ['Divisible' if valor % 2 == 0 else 'No Divisible' for valor in lista]

print(divisible)
#[0, 3, 6, 7, 8, 9]
#['Divisible', 'No Divisible', 'Divisible', 'No Divisible', 'Divisible', 'No Divisible']
# el valor 3 no es divisible por dos
# el valor 6 es divisible por dos

for valor, texto_div in zip(lista, divisible):
    print(f"El {valor} {texto_div} por dos")

lista = ['Lechuga', 'Tomates', True, False, 5.1, 5, 'Otro']

lista_str = [elemento for elemento in lista if type(elemento) is str]

lista = [
    {
        'nombre': 'Alexander',
        'edad': 39
    },
    {
        'nombre': 'Eliana',
        'edad': 20
    }
]

lista_menores = [elemento for elemento in lista if elemento['edad'] <= 20]

print(lista_menores)

claves = ['nombre','apellido','edad','altura']
valores = ['Juan','Pérez', 33, 1.75]

dicc_persona = {k:v for k, v in zip(claves, valores)}

print(dicc_persona)

pais = ['México', 'Chile', 'Argentina']
cant_usuarios = [70, 50, 55]

dicc_paises = {k:v for k, v in zip(pais, cant_usuarios)}

print(dicc_paises)

menos_60 = [{k:v} for k, v in dicc_paises.items() if v < 60]

print(menos_60)