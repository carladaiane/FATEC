num = int(input('\n Digite um número inteiro:'))

a = num

list = []

while len(list)<=13:

    a = a+1
    list.append(a)

print(list)


if num%2 >0:
    print(f'{num} é impar')
else:
    print(f'{num} é par')


for i in range(len(list)):

    if list[i]%2 >0:
        print(f'{list[i]} é impar')
    else:
        print(f'{list[i]} é par')


