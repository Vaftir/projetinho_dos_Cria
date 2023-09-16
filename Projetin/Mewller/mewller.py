total = int(input("me diga um numero: "))
if total == 0:
    print("não pode ser igual a zero")
else:
    lista = [0, 1]

    while len(lista) < total:
        penultimo = lista[-2]
        ultimo = lista[-1]
        novo = ultimo+penultimo
        lista.append(novo)

for n in lista:
    print(n, end=" ")