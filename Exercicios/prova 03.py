# Faça um aplicativo em Python que leia uma quantidade indeterminada de números positivos
#  e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
#  A entrada de dados deverá terminar quando for lido um número negativo



valor = 0
listaNumeros = []

while valor >= 0:
    valor = int(input("Digite numero positivo: "))
    if(valor>=0):
        listaNumeros.append(valor)
   

ate25 = 0
ate50 = 0
ate75 = 0
ate100 = 0

for num in listaNumeros:
    if(num >= 0 and num <= 25):
        ate25 += 1
    if(num >= 26 and num <= 50):
        ate50 += 1
    if(num >= 51 and num <= 75):
        ate75 += 1
    if(num >= 76 and num <= 100):
        ate100 += 1

print('[0-25] : ', ate25, '\n[26-50]: ', ate50,  '\n[51-75]: ', ate75, '\n[76-100]: ', ate100)