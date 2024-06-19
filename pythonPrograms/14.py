
# Print the lines inputted by user until an empty line is printed
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

for line in lines:
    print(line)
