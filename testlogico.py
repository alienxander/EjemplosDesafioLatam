A = True
B = False
C = True
D = False

resultado = A or C and B or D

print(B and D)
print(A	and	C and C	or D)
print((A and C) and (C or D))
print((A and C) and (B or D))

if not B:
    print("B es falso")
    
if (not (A and B)):
    print("expresión es falsa")