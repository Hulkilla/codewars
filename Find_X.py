n = 15


def find_x(n):
    x = 0
    for i in range(n):
        for j in range(2*n):
            x += j + i
    return x

def find_x_2(n):
    return (n**2)*((n*2)+(n-2))

print(find_x(n))
print(find_x_2(n))
