print("numero 1:")
nota1 = int(input())
print("numero 2:")
nota2 = int(input())
print("numero 3:")
nota3 = int(input())

maior =0

if nota1 > nota2:
    maior = nota1
elif nota2 > nota3:
    maior = nota2
else:
    maior = nota3

print(maior)