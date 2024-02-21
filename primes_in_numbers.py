import math


num = 4001


lista=[2,]
cadena = ""

if num == 1:
    cadena = ""
else:     
    primos = []

    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            primos.append(i)
            num //= i
    if num > 1:
        cadena = f"({num})"
   

    else:

        count = 0

        for i in range(len(primos)):

            if i < len(primos) - 1:
                if primos[i] == primos[i + 1]:
                    count += 1
                elif primos[i] != primos[i + 1] and count != 0:
                    cadena += f"({primos[i]}**{count + 1})"
                    count = 0
                elif primos[i] != primos[i + 1] and count == 0:
                    cadena += f"({primos[i]})"
            elif primos[i-1] == primos[i]:
                cadena += f"({primos[i]}**{count + 1})"
            else:
                cadena += f"({primos[i]})"

print(cadena)


### Solucion buenas prácticas

def primeFactors(n):
    i = 2
    r = ''
    while n != 1:
        k = 0
        while n%i == 0:
            n = n / i
            k += 1
        if k == 1:
            r = r + '(' + str(i) + ')'
        elif k == 0: pass
        else:
            r = r + '(' + str(i) + '**' + str(k) + ')'
        i += 1
        
    return r