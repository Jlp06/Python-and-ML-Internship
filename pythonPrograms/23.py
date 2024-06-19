# Cel to fahrenheit

temp = input("Enter the temperature(Celsius or Fahrenheit: ")

# Extracting the numerical part of the temperature
degree= int(temp[:-1])
# Extracting the convention part of the temperature
convention = temp[-1]

if convention.upper()=="C":
    result = int(round((9*degree)/5+32))
    convention1 = "Fahrenheit"
elif convention.upper()=="F":
    result = int(round((degree - 32) * 5 / 9))
    convention1 = "Celsius"
else:
    print("Input proper convention")
    quit()

print("The temperature in", convention1, "is", result, "degrees.")
