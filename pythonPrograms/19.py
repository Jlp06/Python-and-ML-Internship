# Remove punctuations

string = input("Enter any string with punctuations: ")
print("The original string is: ")

punc = '''!()-[]{};:\,<>./?@#$%^&*_~'''

for elements in string:
    if elements in punc:
        string = string.replace(elements, "")

print("The string after removing punctuations: ", string)
