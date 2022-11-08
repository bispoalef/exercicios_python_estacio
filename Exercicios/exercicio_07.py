
notas = []


notas.append(int(input("digite nota 1: ")))
notas.append(int(input("digite nota 2: ")))
notas.append(int(input("digite nota 3: ")))
notas.append(int(input("digite nota 4: ")))

mensagem = ''

somaNotas = 0
for nota in notas:
    somaNotas += nota

media = somaNotas / 4

print(media)