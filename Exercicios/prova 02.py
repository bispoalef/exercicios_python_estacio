# Faça um aplicativo em Python que leia um número e exiba o dia correspondente da semana.
#  (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer o texto “Valor Inválido

valor = int(input("Digite um valor correspondente a um dia da semana: "))

if(valor == 1):
    print('1-Domingo')
elif(valor == 2):
    print('2-Segunda')
elif(valor == 3):
    print('3-Terça')
elif(valor == 4):
    print('4-Quarta-Feira')
elif(valor == 5):
    print('5-Quinta-Feira')
elif(valor == 6):
    print('6-Sexta-Feira')
elif(valor == 7):
    print('7-Sabado')
else:
    print('Valor Inválido')




