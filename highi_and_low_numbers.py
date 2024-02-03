string = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"


lista = string.split(sep = " ")

for i in range(len(lista)):
    lista[i] = int(lista[i])

maximo = str(max(lista))
minimo = str(min(lista))

resultado = maximo + " " + minimo

print(resultado)
