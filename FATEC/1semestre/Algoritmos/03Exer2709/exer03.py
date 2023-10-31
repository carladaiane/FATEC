""" Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa 
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de 
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos 
necessários para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento """

a = 80000

b = 200000

crescA = 0.03

crescB = 0.015


cont = 0

while a<b:
    a = a+a*crescA
    b = b+b*crescB

    cont = cont+1


print(f'Depois de {cont} a população de A {a:.2f} e População {b:.2f} ')



