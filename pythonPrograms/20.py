# Sum of elements in a list

list1 = [11, 23, 9, 33]

total = 0
element = 0

while element < len(list1):
    total = total + list1[element]
    element += 1

print("The sum of all elements in the given list is: ", total)
