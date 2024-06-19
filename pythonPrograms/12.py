
# Sum of digits of a given number

def sum1(n):
    res = 0
    for digit in str(n):
        res += int(digit)
    return res


num = input("Enter a number: ")
result = sum1(num)
print("The sum of digits of the given number is: ", result)
