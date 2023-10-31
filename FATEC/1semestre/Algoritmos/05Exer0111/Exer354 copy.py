def calc(lala):
        
    if lala%2 >0:
        print(f'{lala} é impar')
    else:
        print(f'{lala} é par')


num = int(input('\n Digite um número inteiro:'))

list = []

while len(list)<=14:

    num = num+1
    list.append(num)

print(list)

calc(num)

for i in range(len(list)):
    calc(list[i])


