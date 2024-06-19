
# Check whether a substring is present in given string
string = "Hello all, Welcome to the first session of Python and ML internship Program"
print(string)
substring = input("Enter any substring from the given string: ")
s = string.split()

if substring in s:
    print("Yes {0} is present in the given string".format(substring))
else:
    print("Error! There is no such substring present in the given string")
