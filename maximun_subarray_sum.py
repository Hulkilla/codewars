
numbers = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]

maxSum = 0
maxTemp = 0

for i in range(0, len(numbers)):
    maxTemp += numbers[i]
    if maxTemp < 0:
        maxTemp = 0
    elif (maxSum < maxTemp):
        maxSum = maxTemp

print(maxSum)
