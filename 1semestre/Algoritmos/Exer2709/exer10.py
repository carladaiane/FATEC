""" 10.Faça um programa que peça um inteiro positivo e o mostre invertido. 
Ex.: 1234 gera 4321 """

num = input('Digite um número inteiro:')

a = num[slice(None, None, -1)]

print(a)