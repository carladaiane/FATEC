import os
import platform

def limpar():
    if (platform.system() == 'Windows'):
        os.system('cls')
    if (platform.system() == 'Linux'):
        os.system('clear')

def qtd(cpf):
    if len(cpf) == 11:
        return True
    else:
        return False

def dig1(cpf):
    soma = []
    listcpf = list(map(int, cpf))
    contador = 11
    for digito in listcpf[0:9]:
        contador -= 1
        mult = digito*contador
        soma.append(mult)

    resultado = (sum(soma[0:9])*10) % 11
    if resultado == 10:
        resultado = 0

    if resultado == listcpf[9]:
        return True
    elif resultado != listcpf[9]:
        return False


def dig2(cpf):
    soma = []
    listcpf = list(map(int, cpf))
    contador = 12
    for digito in listcpf[0:10]:
        contador -= 1
        mult = digito*contador
        soma.append(mult)

    resultado = (sum(soma[0:10])*10) % 11
    if resultado == 10:
        resultado = 0
    if resultado == listcpf[10]:
        return True

    elif resultado != listcpf[10]:
        return False


while True:
    cpf = input('\nDigite seu cpf: \n\n')

    if qtd(cpf) and dig1(cpf) and dig2(cpf) == True:
        print('\n CPF válido')

    elif qtd(cpf) ==False:
        print('\n Necessário 11 dígitos')

    elif (qtd(cpf) or dig1(cpf) or dig2(cpf)) == False:
        print('\n CPF inválido')


    while True:
        resposta = input('\nQuer validar novamente?\n \nDigite sim ou não: \n\n')

        if resposta in "nao":
            limpar()
            print('\nObrigada por usar a plataforma!\n')
            os.system(exit())
            break

        if resposta in "sim":
            limpar()
            break

        if resposta != "sim" or "nao":
            limpar()
            print('\n Por gentileza, responda corretamente para presseguir')