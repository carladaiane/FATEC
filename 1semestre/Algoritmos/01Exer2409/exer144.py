saldomedio = float(input(f'\nDigite seu saldo: ').replace(",","."))

if saldomedio < 501:
    print (f'\nComo seu saldo era de R$ {saldomedio}, você não tera nenhum crédito')

elif (saldomedio >=501) and (saldomedio <= 1000):
    print(f'\nComo seu saldo era de: {saldomedio}, seu crédito será de {saldomedio * 0.3}')

elif (saldomedio >= 1001) and (saldomedio <=3000):
    print(f'\nComo seu saldo era de: {saldomedio}, seu crédito será de {saldomedio * 0.4}')

elif saldomedio >3001:
    print(f'\nComo seu saldo era de: {saldomedio}, seu crédito será de {saldomedio * 0.5}')