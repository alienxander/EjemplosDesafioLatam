

lista = []

lista.append("Hola")

print(lista[0])

dicc = {}

dicc = {"nota": 7}

print(dicc["nota"])

contacto = {
    "nombre": "Alexander",
    "apellido": "Beck",
    "numeros_telefono": [
        {
            "tipo": "casa",
            "numero": "888888"
        },
        {
            "tipo": "celular",
            "numero": "99999999"
        },
        {
            "tipo": "celular",
            "numero": "99999998"
        }
    ]
}

#print(contacto["numeros_telefono"][0]["numero"])

lista_telefonos = contacto["numeros_telefono"]

#telefono_celular = {}


lista_telefonos = contacto["numeros_telefono"]

print([telefono for telefono in lista_telefonos if telefono["tipo"] == "celular"])


telefono_celular_lista = []
for telefono in lista_telefonos:
    if telefono["tipo"] == "celular":
        telefono_celular_lista.append(telefono)

print(telefono_celular_lista)

notas = {
    "daniela": 6,
    "carlos": 7
}

notas.update({"raimund": 7})

print(notas)

print(notas["raimund"])

del notas["raimund"]


#print(notas["raimund"])

print(notas.get("raimund"))

if notas.get("raimund") is None:
    print("Raimund no existe en las notas")

