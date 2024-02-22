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
    contador = 2
    while True:
        telefono_agregar = input(f"Ingrese telefono {contador}: (e para salir)").lower()
        if telefono_agregar != "e":
            contacto[f"telefono{contador}"] = telefono_agregar
            contador += 1
        else:
            break
            
print("Contacto actualizado")
print(contacto)




