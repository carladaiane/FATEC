import math as m

ang = float(input('Digite o ângulo em graus: ').replace(",","."))

rang = ang * 3.14 / 180

if ( (rang > 3.14/2 and rang <= 3.14) or (rang > 3*3.14/2 and rang <= 2*3.14)):
    print(f'\nseno: {m.sin(rang):.2f}')

else:
    print(f'\nco-seno: {m.cos(rang):.2f}')
print (f'\n ') 





