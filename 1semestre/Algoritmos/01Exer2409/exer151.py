peso = float(input('Digite seu peso: ').replace(",","."))

altura = float(input('Digite sua altura: ').replace(",","."))

imc = peso / altura **2

if ( imc < 20):
    print(f'\nAbaixo do peso')
elif imc <=25 :
    print(f'\n Normal')
elif ( imc <=30 ):
    print(f'\n nexcesso de peso ')

elif imc <=35:
    print(f'\n Obesidade')
else:
    print(f'\n Obesidade mórbida')

print(f'\n Seu IMC é {imc:.2f}')