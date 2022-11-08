# 1) Faça um programa em Python que leia um nome do usuário e a sua senha e não aceite a
# senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a solicitar as
# informações.



sair = 0
while sair <= 0:
    nome = input("digite o nome de usuario: ") 
    senha = input("digite o senha: ") 
    if(nome == senha): 
        print('nome e senha nao podem ser iguais.')
    else:
        sair += 1


