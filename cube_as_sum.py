def find_summands(n):
    array = list(range(0, n*2, 2))
    a = (pow(n,3)-sum(array))/n  
    for i in range(len(array)):
        array[i] += int(a)
    return(array)


print(find_summands(1))
print(sum(find_summands(1)))
print(pow(1,3))




    

