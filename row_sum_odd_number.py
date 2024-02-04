import numpy as np

n = 2
a = np.sum(range(n))

final = 0
for i in range(n):
    position = a + 1 + i
    odd = 2 * position - 1
    final +=  odd


print(final)