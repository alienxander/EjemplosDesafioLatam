resultado = -1

def suma_numeros(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    
    return resultado


def filtro(color = "roja", **frutas):
    #global resultado
    resultado = [{k:v} for k, v in frutas.items() if v == color]
    print("Resultado filtro: ", resultado)
    return resultado
    
print("Resultado global antes filtro: ", resultado)
print(suma_numeros(2, 3, 1, 5, 6, 200, 3, 5, 9))
print(filtro(manzana = "roja", uva = "morada", frutilla = "roja", color="morada"))
print("Resultado global despues del filtro: ", resultado)