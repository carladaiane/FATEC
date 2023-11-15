a = 5000
b = 65000

cont = 0

while a<=b:
    a = a +(a*0.1)
    b = b +(b*0.05)

    cont = cont+1

print(cont)