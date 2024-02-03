import numpy as np



def square_up(n):
    lista = [0] * n
    array = np.array(lista)
    array_final = list()
    i = 1
    while i < (n+1):
        array[(n-i)::n] = array[(n-i)::n] + i
        lista_array = list(array)
        array_final.append(lista_array)
        i += 1

    return(sum(array_final, start = []))

print(square_up(2))