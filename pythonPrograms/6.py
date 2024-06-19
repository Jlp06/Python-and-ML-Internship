# Reading content from file and printing to the console
a = str(input("Enter the name of the file with .txt extension: "))  # Ask the user for the path of the file
file2 = open(a,'r')
line = file2.readline()
while line != "":
    print(line)
    line = file2.readline()
file2.close()
