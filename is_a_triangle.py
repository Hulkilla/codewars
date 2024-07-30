def is_triangle(a,b,c):
    return isinstance(a, int) and isinstance(b, int) and isinstance(c, int) and (a+b) > c and (a+c) > b and (c+b) > a
        

print(is_triangle(1.2,2,2))
    

