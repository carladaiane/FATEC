""" Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido. """

nota = 100

while nota <0 or nota >10:
    nota = float(input('\n Digite uma nota entre zero e dez:'))

    if nota <0 or nota >10:
        print('\n Nota Inválida')

print('\n Nota válida')