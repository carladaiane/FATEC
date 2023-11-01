lista = []
cont = 0

while len(lista)<=9:

    cont = cont+1

    num = int(input(f'\nDigite o {cont}º valor: '))

    lista.append(num)
    
    print(sorted(lista, reverse=True))
