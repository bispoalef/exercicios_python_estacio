# 5. Fazer um programa em Pyrhon que receba um valor de salário atual de um funcionário e calcule o valor do novo salário
#  reajustando de acordo com a tabela abaixo descrita abaixo: (_____ de 2,0 pontos)
# Salário atual	Reajuste
# Abaixo de R$700,00	20%
# de R$700,00 até R$1000,00	10%
# Acima de R$1000,00	5%




def funcao(salarioAtual):
    novoSalario = 0
    if(salarioAtual <= 700):
        novoSalario = salario + (salarioAtual * 0.20)
    elif(salarioAtual > 700 or salarioAtual <= 1000):
        novoSalario = salario + (salarioAtual * 0.10)
    else:
        novoSalario = salario + (salarioAtual * 0.5)

    return novoSalario


salario = int(input("Digite o Salario atual: "))

novoSalario = funcao(salario)
print('Salario pós reajuste: ' , novoSalario)