# Operadores aritméticos
"""
*: multiplicación
**: exponente
/: División
//: Cuociente 3.5 -> 3
%: Módulo --> El resto de una división
+: Suma
-: Resta
"""

print("2 elevado a 2: ", 2**2)

print(f"1/9: \nResultado: {9/8:.2f}\nCuociente: {9//8}\nResto o módulo: {9%8}")

#Precedencia de operaciones
resultado = 2 + 3 / 5
print("Resultado1: ", resultado)
resultado = (2 + 3) / 5
print("Resultado2: ", resultado)
resultado = int((2 + 3) / 5)
print("Resultado3: ", resultado)
resultado = (2 + 3) // 5
print("Resultado4: ", resultado)
resultado = (5 + 5) / (1 + 1)
print("Resultado5: ", resultado)
resultado = (5 + 5 + (3 * 2)) / (1 + 1 * (5 + 5))
"""
(3*2) = 6
5 + 5 = 10
16 --> 1

(5 + 5) = 10
1 * 10 = 10
1 + 10 = 11 --> 2

16/11 = 1.45

"""
print("Resultado6: ", resultado)