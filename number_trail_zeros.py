import math
n = 699499205

if n == 0:
    print(0)
else:
    kmax = math.trunc(math.log(n,5))

    z = 0
    for i in range(1, (kmax+1)):
        term = n / pow(5, i)
        z += math.trunc(term)

    print(z)


