""" Criar um algoritmo que armazene 10 números em um vetor. 
Na entrada de dados, o número já deverá ser armazenado na sua posição
definitiva em ordem decrescente.
Imprimir o vetor logo após a entrada de dados. """

lista = [34,25,70,89]

""" num = int(input('\nDigite um número: '))

lista.append(num) """
 
aaa = lista.sort(key=int, reverse=True) 

print(aaa)