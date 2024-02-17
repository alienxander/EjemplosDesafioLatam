import sys
import time
from fcustom import limpiar_consola

i = int(sys.argv[1])
c = 0
limpiar_consola()
while i >= 0:
    print(i)
    time.sleep(1)
    limpiar_consola()
    i -= 1

chrpunto = "."

while c <= 10:
    print(chrpunto)
    time.sleep(1)
    limpiar_consola()
    chrpunto += "."
    c += 1
    
print("Booom !!!")