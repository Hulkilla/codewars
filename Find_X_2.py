import numpy as np
def find_x(n):
      if n == 0: return 0
      x = 0
      for i in range(1, n+1):
            x += find_x(i-1) + 3*i
      return x

print(find_x(5))

M = 10 ** 9 + 7
def find_x_2(n):
    return 3 * (pow(2, n + 1, M) - n - 2) % M



print(find_x_2(5))