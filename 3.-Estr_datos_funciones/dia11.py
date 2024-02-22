#Practica
contacto = {
    "nombre": "",
    "apellido": "",
    "telefono1": ""
}

# contacto = {
#     "nombre": "Alex",
#     "apellido": "Beck",
#     "telefono1": "23212",
#     "telefono2": "124141",
#     "telefono3": "13435",
#     "telefono4": "325252",
# }

#contacto["telefono2"] = ""

contacto["nombre"] = input("Ingrese el nombre: ")
contacto["apellido"] = input("Ingrese el apellido: ")
contacto["telefono1"] = input("Ingrese telefono principal: ")

while True: 
    tiene_mas_telef = input("Tiene más telefonos que agregar? (s/n)").lower()
    if tiene_mas_telef != "s" and tiene_mas_telef != "n":
        print("Ingrese un valor válido (s/n)")
    else:
        break
    
if tiene_mas_telef == "s":
    cantidad_telef = input("Ingrese la cantidad de telefonos (Debe ser mayor a 1): ")
    while not (cantidad_telef.isdigit() and type(int(cantidad_telef)) and int(cantidad_telef) > 1):
        if not (cantidad_telef.isdigit() and type(int(cantidad_telef)) and int(cantidad_telef) > 1):
            print("Ingrese una cantidad de télefonos válida. Esta debe ser númerica y mayor a 1")
            cantidad_telef = input("Ingrese la cantidad de telefonos: ")
            
    for i in range(int(cantidad_telef)):
        contacto[f"telefono{i + 2}"] = input(f"Ingrese telefono {i + 2}")

print("Contacto actualizado")
print(contacto)




