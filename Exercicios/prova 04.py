# 4. Faça um programa que solicite a altura e a idade de 3 pessoas,
#  armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida


listaPessoas = []


cont = 1
while cont <= 3:
    altura = int(input('Altura da pessoa em centímetros: '))
    listaPessoas.append(altura)
    idade = int(input('Idade: '))
    listaPessoas.append(idade)
    cont += 1

listaInvertida = listaPessoas[:: -1]
print(listaInvertida)
