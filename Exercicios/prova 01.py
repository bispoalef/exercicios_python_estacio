# 1. Faça um aplicativo que receba um valor inteiro, informe se é mesmo é um número é negativo, positivo ou neutro.

valor = int(input("digite um valor inteiro: "))

if(valor > 0):
    print('Numero positivo')
elif(valor < 0):
    print('Numero negativo')
else:
    print('Numero neutro')


