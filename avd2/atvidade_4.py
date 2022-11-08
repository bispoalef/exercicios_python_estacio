# 4) Faça um programa em Python que peça um número inteiro positivo e em seguida apresente
# este número invertido.
# Exemplo:
# 32376487 => 78467323


def reverso(val):
    num = str(val)

    return num[::-1]

numero = int(input("digite um numero inteiro: ")) 
print(numero, ' => ', reverso(numero))

