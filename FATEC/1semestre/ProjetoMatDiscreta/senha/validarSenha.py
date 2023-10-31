import os
import platform

ce1 = list(map(chr, range(33, 48)))
ce2 = list(map(chr, range(58, 65)))
ce3 = list(map(chr, range(91, 97)))
ce4 = list(map(chr, range(123, 127)))
ce5 = list(map(chr, range(123, 127)))
ce = ce1+ce2+ce3+ce4+ce5

def limpar():
    if (platform.system() == 'Windows'):
        os.system('cls')
    if (platform.system() == 'Linux'):
        os.system('clear')

def minus(senha):
    for valor in list(map(chr, range(97, 123))):
        if valor in senha:
            return True
    return False

def maius(senha):
    for valor in list(map(chr, range(65, 91))):
        if valor in senha:
            return True
    return False

def qtd(senha):
    if (len(senha) >= 8):
        return True
    return False

def numero(senha):
    for valor in list(map(chr, range(48, 58))):
        if valor in senha:
            return True
    return False

def especial(senha):
    
    for valor in ce:
        if valor in senha:
            return True
    return False

while True:

    print('\nOlá!\n\nPara criar uma senha forte ela deve ter no mínimo:\n\n - 8 caracteres\n - 1 letra maius\n - 1 letra minus\n - 1 caractere especial\n - 1 número\n')
    senha = input('\nDigite sua senha: ')
    
    limpar()

    if minus(senha) == False:
        a = print(f'\nSenha Inválida: Necessário 1 letra minúscula')
    if maius(senha) == False:
        a = print(f'\nSenha Inválida: Necessário 1 letra maius')
    if qtd(senha) == False:
        a = print(f'\nSenha Inválida: Quantidade mínima de caracter é 8')
    if numero(senha) == False:
        a = print(f'\nSenha Inválida: Necessário 1 número')
    if especial(senha) == False:
        a = print(f'\nSenha Inválida: Necessário 1 caracter especial')
    
    if minus(senha) and maius(senha) and qtd(senha) and especial(senha) and numero(senha) == True:
            print(f'\n \nSenha Aceita!\n')
            break

    while True:
        resp = input(f'\nQuer tentar novamente?\nResponda sim ou não:').lower()
    
        if  resp in "nao":
            limpar()
            print(f'\n \nObrigada por usar a plataforma!\n')
            os.system(exit())
            break
            
        if resp != "sim" or "nao":
            limpar()
            print(f'\nPor gentileza, responda para presseguir')

        if resp in "sim":
            limpar()
            break
