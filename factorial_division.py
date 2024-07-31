from functools import reduce

def factorial_division(a,b):

    if a > b and a >= 0 and b >= 0:
        if a == b or a == 0 or b == 0:
            return 1
        return reduce(lambda x, y: x * y, range(b + 1, a + 1), 1)


print(factorial_division(5,4))

'''
 Python program to find the factorial of a number provided by the user using recursion

def factorial(x):
    """This is a recursive function to find the factorial of an integer"""

    if x == 0 or x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


# change the value for a different result
num = 7

# to take input from the user
# num = int(input("Enter a number: "))

# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)'''

