a = [20, 7, 6, 2]

a.sort()
a.reverse()

array1 = list()
array2 = list()

for i in range(len(a)):
    if i % 2 == 0:
        array1.append(a[i])
    else:
        array2.append(a[i])


array2.reverse()
lista = array1 + array2
print(lista)



def make_valley(a):
    numero = len(a)
    lista = [0]  * len(a)
    a.count(0)
    i = 0
    posicion = 0
    if len(a) % 2 == 0:
        while i < numero:
            if lista.count(0) == len(lista):
                lista[i] = max(a)
            elif lista.count(0) % 2 != 0:
                num2 =len(lista)-posicion
                lista[int(num2)] = max(a)
            elif lista.count(0) % 2 == 0:
                lista[int(posicion)] = max (a)
            elif a.count(0) == len(a):
                break

            a[a.index(max(a))] = 0
            i +=1
            posicion +=0.5

    elif len(a) % 2 != 0:
        while i < numero:
            if lista.count(0) == len(lista):
                lista[i] = max(a)
                print(a)
            elif lista.count(0) % 2 == 0:
                num2 =len(lista)-posicion
                lista[int(num2)] = max(a)
                print(a)
            elif lista.count(0) % 2 != 0:
                lista[int(posicion)] = max (a)
                print(a)
            elif a.count(0) == len(a):
                print(a)
                break

            a[a.index(max(a))] = 0
            i +=1
            posicion +=0.5

    return lista

#print(make_valley(a))
