


preguntas = ['Pregunta 1', 'Pregunta 2', 'Pregunta 3']

def hacer_preguntas():
    respuestas = []
    for pregunta in preguntas:
        print(pregunta)
        print("Opciones")
        print("1. De acuerdo")
        print("2. Desacuerdo")
        print("3. Indiferente")
        respuestas.append(input("Respuesta: "))
    
    return respuestas


lista_respuesta = hacer_preguntas()
dict_respuestas = [{k:'De Acuerdo' if v == '1' else 'Desacuerdo' if v == '2' else 'Indiferente'} for k, v in zip(preguntas, lista_respuesta)]

lista_dict = []
for k, v in zip(preguntas, lista_respuesta):
    valor_clave = ""
    if v == "1":
        valor_clave = "De Acuerdo"
    elif v == "2":
        valor_clave = "Desacuerdo"
    else:
        valor_clave = "Indiferente"
    
    lista_dict.append({
        k: valor_clave
    })

print("Lista dict con comprhension: ", dict_respuestas)
print("Lista dict sin comprhension: ", lista_dict)






