op = int(input(f'\nDigite 1- Regiao Norte 2- Regiao Nordeste 3- Regiao Centro-Oeste 4-Regiao Sul: '))

iv = int(input(f'\nDigite 1- Ida 2- Ida e Volta:'))

if(op == 1) and (iv == 1):
    print(f'\n O valor da passagem de ida para R.Norte R$500.00')
elif (op == 1) and (iv == 2):
    print(f"\nO valor da passagem de ida-volta para R.Norte: R$900.00")
elif (op == 2) and (iv == 1):
    print(f'\nO valor da passagem de ida para R.Nordeste: R$350.00')
elif(op == 2) and (iv == 2):
    print(f'\nO valor da passagem de ida-volta para R.Nordeste: R$650.00')
elif (op == 3) and (iv == 1):
    print(f'\nO valor da passagem de ida para R.C.Oeste: R$350.00')
elif (op == 3) and (iv == 2):
    print(f'\nO valor da passagem de ida-volta para R.C.Oeste: R$600.00')
elif (op == 4) and (iv == 1):
    print(f'\nO valor da passagem de ida para R.Sul: R$300.00')
elif  (op == 4) and (iv == 2):
    print(f'\nO valor da passagem de ida-volta para R.Sul: R$550.00')
else:
    print('\nOpcao Inexistente')



