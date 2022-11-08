def sub():
    print("Primeira nota:")
    nota1 = input()
    print("Segunda nota:")
    nota2 = input()

    media = (int(nota1) + int(nota2)) / 2
    print(media)
    if media >= 7:
        print('Aprovado')
    if media < 7:
        print('Reprovado')
    if media == 10.0:
        print('Aprovado com Distinção')

sub()