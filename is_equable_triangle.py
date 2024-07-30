from math import sqrt
def equable_triangle(a,b,c):
    if (a+b) > c and (a+c) > b and (c+b) > a:
        perimeter = a + b + c
        s = perimeter/2
        area = sqrt(s*(s-a)*(s-b)*(s-c))
        return perimeter == area
    return False

print(equable_triangle(7,15,20))