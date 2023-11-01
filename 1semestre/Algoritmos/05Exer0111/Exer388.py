""" Criar um algoritmo que armazene 10 números em um vetor. 
Na entrada de dados, o número já deverá ser armazenado na sua posição
definitiva em ordem decrescente.
Imprimir o vetor logo após a entrada de dados. """

lista = []

cont = 0

while len(lista)<=9:

    cont = cont+1

    num = int(input(f'\nDigite o {cont}º valor: '))

    lista.append(num)
    
    print(sorted(lista, reverse=True))
