import sys
import random
import time
from fcustom import limpiar_consola

jugador = ""

limpiar_consola()

c = 0
mensaje_salida = "Ingrese un parámetro válido"
if len(sys.argv) == 2:
    jugador = sys.argv[1].lower()
else:
    while c <= 5:
        limpiar_consola()
        print(mensaje_salida)
        time.sleep(0.5)
        mensaje_salida += "."
        c += 1
        if c == 5:
            print("Saliendo del sistema")
            sys.exit()
        
while (jugador != 'piedra' and jugador != 'papel' and jugador != "tijeras"):
    print('Argumento inválido. Debe Ingresar piedra, papel o tijeras')
    jugador = input("Ingrese su jugada (piedra, papel, tijeras)")

computador = random.choice(['piedra', 'papel', 'tijeras'])
resultado = ""

##if()##

print(f'''
      Tu jugaste {jugador}
      Computador jugó {computador}''')


    