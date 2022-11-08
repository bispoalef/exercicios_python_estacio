# 2) Faça um programa que imprima na tela os números de 1 a 10, um abaixo do outro. Depois
# modifique o programa para que ele mostre os números um ao lado do outro.


count = 1

while count <= 10:
    print(count)
    count +=1


num = []

count2 = 1

while count2 <= 10:
    num.append(count2)
    count2 +=1

print(num)