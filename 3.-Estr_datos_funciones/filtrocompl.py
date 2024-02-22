dicc_mascotas = {
    "perro": 3,
    "gato": 4,
    "tortuga": 6,
    "conejo": 6
}

# conejo = [v for k, v in dicc_mascotas.items() if k == "conejo"]
# print(conejo)

dicc_mascotas_aumento = {k:(v + 5) for k, v in dicc_mascotas.items() if k == "perro"}
dicc_mascotas_restantes = {k:(v + 5) for k, v in dicc_mascotas.items() if k != "perro"}
dicc_mascotas_aumento.update(dicc_mascotas_restantes)

dicc_mascotas["perro"] = dicc_mascotas["perro"] + 4
dicc_mascotas["perro"] +=8

print(dicc_mascotas) 


print("aumen 5: ", dicc_mascotas_aumento)

mayores_6 = [{k:v} for k, v in dicc_mascotas.items() if v >= 4]
print(mayores_6)
for k, v in dicc_mascotas.items():
    print(k, v)
    

ventas_mes = ['Octubre', 'Noviembre', 'Diciembre']
ventas_montos = [65000, 68000, 76000]

dicc_ventas = {k:v for k, v in zip(ventas_mes, ventas_montos)}

print(dicc_ventas)