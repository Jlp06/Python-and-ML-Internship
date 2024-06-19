# Write a python program that returns the minimum and maximum values in a list of numbers.

my_list = eval(input("Enter a list of numbers: "))
large = my_list[0]
small = my_list[0]

for num in my_list:
    if num > large:
        large = num
    if num < small:
        small = num

print("The largest number in the list is: ", large)
print("The smallest number in the list is: ", small)
