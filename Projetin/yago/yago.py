
# Fubbonacci a b c sendo que  c=a+b
até_onde_vai = 10
a = 0
b = 1
c = b
contador = 1

while contador <= até_onde_vai:
    print(c, end=" ")
    contador += 1
    a, b = b, c
    c = a + b

print()