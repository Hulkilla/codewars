
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxSum = 0
maxTemp = 0

for i in range(0, len(numbers)):
    maxTemp += numbers[i]
    if maxTemp < 0:
        maxTemp = 0
    elif (maxSum < maxTemp):
        maxSum = maxTemp
    print(numbers[i], maxSum, maxTemp)

    
print(maxSum)
