# 5) Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a
# quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais
# de 40 alunos.



sair = 0

while sair == 0:

    quantidadeTurma = int(input("Qual a quantidade de turmas: ")) 
    numeroAlunos = int(input("Quantidade total de alunos: ")) 


    totalDeAlunosPorTurma = numeroAlunos / quantidadeTurma


    if(totalDeAlunosPorTurma >= 40):
        print('O numero de alunos por sala nao pode ser maior que 40! por favor aumentre o numero de salas....')
    else:
        sair +=1

    
print('Quantidade de alunos por sala: ', int(totalDeAlunosPorTurma))