lista = []

cont = 0

while len(lista)<=9:

    cont = cont+1

    num = int(input(f'\nDigite um número o {cont}º: '))

    lista.append(num)
    
    print(sorted(lista, reverse=True))