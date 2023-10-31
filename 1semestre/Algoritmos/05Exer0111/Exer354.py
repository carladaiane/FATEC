num = int(input('\n Digite um número inteiro:'))

if num%2 >0:
    print(f'{num} é impar')
else:
    print(f'{num} é par')

list = []

while len(list)<=13:

    num = num+1
    list.append(num)

print(list)


for i in range(len(list)):

    if list[i]%2 >0:
        print(f'{list[i]} é impar')
    else:
        print(f'{list[i]} é par')


