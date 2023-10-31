nome = input('\nDigite seu nome:')

idade = int(input('\nDigite sua idade:'))


if (idade <= 10 ):
    print(f"\n {nome}, você pagará R$ 30, 00")
elif (idade <= 29 ):
    print(f"\n {nome}, você pagará R$ 60,00")
elif(idade <= 45 ):
    print( f"\n, {nome}, você pagará R$ 120,00")
elif (idade <= 59 ):
    print(f'\n {nome}, você pagará R$ 150,00')
elif (idade <= 65 ):
    print(f'\n {nome}, você pagará R$ 250,00')
else:
    print(f'\n  {nome}, você pagará R$ 400,00')
