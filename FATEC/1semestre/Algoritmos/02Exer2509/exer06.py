""" Dizemos que um número natural é triangular se ele é produto de três números naturais
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n,
verificar se N é triangular.
 """

n = input('Digite um numero:')


calculo_nr_triangular = 0

y = 1

while calculo_nr_triangular < n:
    calculo_nr_triangular = y*(y+1)*(y+2)
    y+=1 # ou y = y+1

if calculo_nr_triangular == n:
    print(f'É tringular')

else:
    print(f'Não é tringular')