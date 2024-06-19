# Write a python program that counts the occurrences of a specific element in a list.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 2, 3, 7, 8, 4, 5]
print("The given list is: ", my_list)

num = int(input("Enter any number from the list to be counted: "))
count = my_list.count(num)

print("The count of the given number is: ", count)
