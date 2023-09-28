""" 
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. """

usuario = input('\n Digite seu usuário:')

senha = input('\n Digite sua senha:')

while senha == usuario:
    print('Senha inválida')
    usuario = input('\n Digite seu usuário:')

    senha = input('\n Digite sua senha:')
    

print('Senha')
