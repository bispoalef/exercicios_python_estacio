# 3) Numa eleição existem cinco candidatos. Faça um programa em Python que peça o número
# total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada
# candidato.


lula = 0
bolsonaro = 0
ciro = 0
simone = 0
padre = 0



totalEleitores = int(input("Digite a quantidade de eleitores: ")) 

print('Digite \n 1 para lula \n 2 bolsonaro  \n 3 ciro  \n 4 simone  \n 5 padre')

count = 1
while count <= totalEleitores:
    voto = int(input("Digite: ")) 

    if(voto == 1):
        lula +=1
    elif(voto == 2):
        bolsonaro += 1
    elif(voto == 3):
        ciro += 1
    elif(voto == 4):
        simone += 1
    elif(voto == 5):
        padre += 1
    else:
        print('voto nulo')
    
    count += 1


print('Placar da votação: ')
print('lula: ' , lula)
print('bolsonaro' , bolsonaro)
print('ciro' , ciro)
print('simone' , simone)
print('padre' , padre)
