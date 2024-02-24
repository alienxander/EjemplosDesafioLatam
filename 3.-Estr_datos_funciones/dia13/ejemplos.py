

# def suma_numeros(a = 2, b = 2):
#     return a + b

# def filtro_dict(diccionario:dict, criterio):
#     dicc_filtro = [{k:v} for k, v in diccionario.items() if v == criterio]
#     dicc_filtro_none = [{k:'None' if v != criterio else v} for k, v in diccionario.items()]
#     return dicc_filtro, dicc_filtro_none


# def filtro_dict_sin_c(diccionario:dict, criterio):
#     dicc_result = {}
#     for k, v in diccionario.items():
#         if v != criterio:
#             dicc_result.update(
#                 {
#                     k: 'None'
#                 }
#             )
#         else:
#             dicc_result.update(
#                 {
#                     k: v
#                 }
#             )
    


# n1 = 3
# n2 = 5

# resultado = suma_numeros(n1, n2)

# resultado = 0 if resultado < 8 else resultado
# #resultado = 8
# resultado = suma_numeros()
# #resultado = 4

# dicc_original_filtro, dicc_original_none = filtro_dict({'Pepito': 10, 'Pepita': 10, 'Alexander': 1}, 10)
# dicc_original_filtro, dicc_original_none = filtro_dict(1, 10)

# print(dicc_original_filtro, dicc_original_none)

# def funct1():
#     return 2, 3, 4, 5


# print(funct1())

# mi_join = ';'.join(['Hola', 'como', 'estás'])

# print(mi_join)


# def suma(a, b):
#     return a + b


# def potencia(mi_funcion, exponente):
#     resultado = mi_funcion(exponente, exponente)
#     return resultado**exponente


# res_potencia = potencia(3, 3)
# print(res_potencia)



def saludo(func_despedida):
    print("Hola y")
    func_despedida()

def despedida():
    print("chao")
    
saludo(despedida)


