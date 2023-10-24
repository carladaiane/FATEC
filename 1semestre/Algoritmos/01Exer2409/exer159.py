import math as m

x = float(input('Digite valor de x:').replace(",","."))

if(x > 4. or x < (-4.)):
    fx = (5 * x + 3 ) / m.sqrt((x**2 -16))
    print(f"\nf(x) = {fx:.2f}") 

else:
    print(f'\nNÃO PODE SER FEITA')

