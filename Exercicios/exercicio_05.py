numero = int(input("digite um número: "))


cont = 1
soma = []
while cont <= numero:
    soma.append(cont)
    cont += 1

for valor in soma:
    print(valor)