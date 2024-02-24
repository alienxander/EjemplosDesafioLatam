def mi_funcion(*params):
    return params

print(mi_funcion(1, 2, "Hola"))

def mi_funcion_2(**params):
    return params

print(mi_funcion_2(param1=1, param=2, saludo="Hola"))

var_global = "Hola mundo"

def mi_funcion_3():
    global var_global
    var_global = "Chao mundo"
    print(var_global)
    
mi_funcion_3()
print(var_global)

def mi_funcion_4(param) -> int:
    return param, "HOla"

def mi_funcion_5(param):
    return param("chao chao")

print(mi_funcion_5(mi_funcion_4("Hola hola")))


