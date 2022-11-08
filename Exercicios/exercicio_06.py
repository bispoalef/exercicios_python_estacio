

texto = input("digite algo: ")

num = 0
letras = 0

for char in texto:
    if(char.isdigit()):
        num += 1
    if(char.isalpha()):
        letras += 1

print('Quantidade de numeros: ' , num)       
print('Quantidade de letras: ' , letras)       