# Factorial of a given number
def factorial(n):  # Function for factorial
    res = 1   # Initialize the first number to be multiplied with as 1
    for i in range(2, n + 1):
        res *= i
    return res


num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
