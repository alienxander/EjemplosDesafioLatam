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

lista_castigo = [alumno for alumno in lista_alumnos if alumno["nota"] == 7]


print(lista_castigo)