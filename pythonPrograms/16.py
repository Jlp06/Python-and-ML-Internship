
# Frequency of each character in string
string = input("Enter any string: ")
freq = {}
for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Count of all the characters in the string: ", str(freq))
