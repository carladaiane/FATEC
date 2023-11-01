banco = []

while len(banco)<=20:

    if len(banco)==20:
        print('\n ATENÇÃO!! Limite máximo de registro de cheque atingido')
        break
        
    num = input('\n Digite o numero do cheque: ')
    valor = input('\n Digite o valor do cheque: ')
    data = input('\n Digite a data do cheque: ')
    destino = input('\n Digite o destinoo cheque: ')

    banco.append({"num":num, "valor":valor, "data":data, "destino": destino})

    print('\n Cheque cadastrado com sucesso!!')

    resp = input('\n Deseja cadastrar outro?(s ou n):')

    if resp in 'nãao':
        break
    
    else:
        True

cont = 0
print('\n')
print('\nRelatório\n')
for dicionario in banco:
    cont = cont+1
    print('----------------------------------------')
    print(f'\n Cheque ID {cont}\n')
    print(f"N°: {dicionario['num']}")
    print(f"Valor: {dicionario['valor']}")
    print(f"Data: {dicionario['data']}")
    print(f"Destino: {dicionario['destino']}")
    print('\n')
