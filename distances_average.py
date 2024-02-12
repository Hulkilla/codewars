from statistics import mean

array = [55, 95, 62, 36, 48]

array_2 =[]
for i in range(len(array)):
    array_2.append(round(array[i] - mean(array),1))

print(array_2)