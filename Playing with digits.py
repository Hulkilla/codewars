number = 92
p = 1

suma = 0
for i in range(len(str(number))):
    suma += (int(str(number)[i])) ** (p + i)
    
if suma % number == 0:
    print(suma/number)
else: 
    print(-1)
