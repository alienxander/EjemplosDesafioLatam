precio1 = int(input("Ingrese precio producto 1: "))
precio2 = int(input("Ingrese precio producto 2: "))
precio3 = int(input("Ingrese precio producto 3: "))

total = precio1 + precio2 + precio3
print("Total antes del redondeo: ", total)
ultimo_dig = int(str(total)[len(str(total)) - 1])

if(ultimo_dig >= 1 and ultimo_dig < 5):
    total = str(total)[0:str(total).__len__() - 1] + "0"
else:
    total = str(total)[0:str(total).__len__() - 2] + str(int(str(int(str(total)[str(total).__len__() - 2]) + 1))) + "0"

print("Total Boleta: ", total)