import math as m

ang = float(input('Digite o ângulo em graus: ').replace(",","."))

rang = ang * m.pi / 180

if ((rang > m.pi / 2 and rang <= m.pi) or (rang > 3 * m.pi / 2 and rang <= 2 * m.pi)):
    print(f'\nseno: {m.sin(rang):.2f}')

else:
    print(f'\nco-seno: {m.cos(rang):.2f}')
print (f'\n ') 
