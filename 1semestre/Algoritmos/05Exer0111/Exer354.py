num = int(input('\n Digite um número inteiro:'))

list = []

while len(list)<=14:

    num = num+1
    list.append(num)

for elemento in range(list):

    if list[elemento]%2 >0:
        print(f'{list[elemento]} é impar')
    else:
        print(f'{list[elemento]} é par')


