import math as m

ang = float(input('Digite o ângulo em graus: ').replace(",","."))

rang = ang * math.pi / 180

if ((rang > math.pi / 2 and rang <= math.pi) or (rang > 3 * math.pi / 2 and rang <= 2 * math.pi)):
    print(f'\nseno: {m.sin(rang):.2f}')

else:
    print(f'\nco-seno: {m.cos(rang):.2f}')
print (f'\n ') 





