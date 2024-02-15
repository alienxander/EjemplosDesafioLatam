'''
remuneracion: 1.000.000
que tenga beneficio de almuerzo o que tenga un bono de desempeño
que sea trabajo remoto o a al menos tenga 4 dias en remoto
tenga beneficios para los hijos
'''
expect_ingreso = int(input("Ingrese expectativa de ingreso: "))
remuneracion = int(input("Ingrese remuneración: "))
benef_almuerzo = str(input("Tiene beneficio de almuerzo (S / N): ")).upper()
benef_bono_desempenio = str(input("Tiene bono desempeño (S / N): ")).upper()
tiene_trabajo_remoto = str(input("Es remoto (S / N): ")).upper()

if tiene_trabajo_remoto == "S":
    modalidad_hibrida = "5"
else:
    modalidad_hibrida = str(input("Ingrese la modalidad híbrida (ej: 4x1 - 4 dias remotos y 1 dia oficina): "))[0]
    
benef_hijos = str(input("Tiene beneficios para los hijos (S / N): ")).upper()

#modalidad_hibrida_arr = modalidad_hibrida.split("x")
#modalidad_hibrida_arr = modalidad_hibrida[0]

if remuneracion >= expect_ingreso and (benef_almuerzo == "S" or benef_bono_desempenio == "S") and int(modalidad_hibrida) >= 4 and benef_hijos == "S":
    print("Quiero el trabajo")
else:
    print("NO Quiero el trabajo")