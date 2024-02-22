from time import sleep
from fcustom import limpiar_consola

load = "/-\\"
ciclo = ""

for i in range(10):
    for char_load in load:
        print("\033[1;33;32m" + ciclo + char_load + "\033[0;m")
        sleep(0.5)
        limpiar_consola()
    ciclo = ciclo + "."

limpiar_consola()
print("\033[1;33;32m" + ciclo + char_load + "\033[0;m" + "(OK)")