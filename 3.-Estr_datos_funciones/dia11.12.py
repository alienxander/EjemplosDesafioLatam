contacto = {
    "nombre": "Alien",
    "apellido": "Beck",
    "telefono1": "99999"
}

print(contacto.keys())

for k in contacto.keys():
    print(k)
    
print(contacto.items())

for k, v in contacto.items():
    print(f"{k}: {v}")
    
print(contacto.values())

for v in contacto.values():
    print(v)
    
print("Telefono 1: ", contacto.get("telefono1"))
print("Telefono 1: ", contacto.get("telefono2"))
#print("Telefono 1: ", contacto["telefono2"])
print("Telefono 1: ", contacto.get("telefono2", "El telefono 2 no exite"))

#Tuplas

mi_tupla = ('Perro', 12, "Gato", 23)

print(type(mi_tupla))

animal1, cantidad1, animal2, cantidad2 = mi_tupla

print(animal1, cantidad1, animal2, cantidad2)

#sets - es un conjumto de valore sin claves e irrepetibles

mi_set = {"Oro", "Plata", "Niquel", "Bronce", "Uranio", "Cobre", "Boro", "Plata", "Niquel"}


mi_set.add("Carbono")

print(mi_set)

notas = {
    "Camila": 9,
    "Orihana": 10,
    "Carlos": 10,
    "Raimund": 10
}


print(notas)

lista_notas = list(notas.items())

print(lista_notas)

print(lista_notas[0][0])
print(lista_notas[0][1])

for nota in lista_notas:
    if nota[1] < 10:
        print(nota)

menores_10 = [nota for nota in lista_notas if nota[1] < 10]

print(menores_10)

#Lista en dicc
menores_10_dicc = dict(menores_10)
print(menores_10_dicc)

#otra = dict([1, 2, 3])
otra = dict([("hola", 1), ("chao", 3)])
print(otra)

#Diccionarios a tuplas
print(notas)
print("Dicc notas en tupla: ", tuple(notas))

#Diccionarios a sets

print(set(notas))

mi_string = "Hola mundo"

#print(dir(mi_string))
#print(dir(lista_notas))

#print(mi_string.__dir__())

#sum, min, max

print(sum([1, 2, 3]))
print(min([1, 2, 3]))
print(max([1, 2, 3]))
print("Max: ", min(["Hola", "Chao", "Beck"]))
#notas_suma = sum([nota[1] for nota in lista_notas]) / len(lista_notas)

print(lista_notas)

promedio_curso = sum([nota[1] for nota in lista_notas]) / len(lista_notas)

print(promedio_curso)


