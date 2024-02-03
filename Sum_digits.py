digit = -4567

suma = 0
for i in range(len(str(digit))):
    if str(digit)[i] == "-":
        pass
    else:
       suma += (int(str(digit)[i]))

print(suma)