contacto = {
    "nombre": "Alexander",
    "apellido": "Beck",
    "numeros_telefono": [
        {
            "tipo": "casa",
            "numeros": [
                "1111111",
                "2222222"
            ]
        },
        {
            "tipo": "celular",
            "numeros": [
                "8888888",
                "5555555",
                "9999999"
            ]   
        }
    ]
}

texto = "hola chao como estas hola chao de nuevo"

def get_numeros(clave:str):
    return [numeros for numeros in contacto["numeros_telefono"] if numeros["tipo"] == clave][0]


def get_cuenta_texto(separador = " "):
    n_caracteres_totales = len(texto)
    n_caracteres_distintos = len(set(texto))
    n_palabras_totales = len(texto.split(separador))
    n_palabras_distintas = len(set(texto.split(separador)))
    return n_caracteres_totales, n_caracteres_distintos, n_palabras_totales, n_palabras_distintas

def dict_filter():
    pass


print(get_numeros("celular"))
print(get_numeros("casa"))
print(get_cuenta_texto())
print(get_cuenta_texto("-"))
dict_filter()









# for k, v in dict(numeros_celular[0]).items():
#     print(k, v)

#print(numeros_celular)
#print(numeros_celulat_dicc)

# for numeros in contacto["numeros_telefono"]:
#     for numero in numeros["numeros"]:
#         print(numeros["tipo"] + ": " + numero)

