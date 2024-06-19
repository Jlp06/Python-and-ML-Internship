
# Program to generate the first n numbers in Fibonacci sequence
num = int(input("Enter a number: "))
n1, n2 = 0, 1
print("The fibonacci sequence is: ", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

