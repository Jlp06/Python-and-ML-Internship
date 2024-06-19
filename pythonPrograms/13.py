
# Age calculator
def calc_age(year):
    present_year= 2024
    result = present_year - year
    return result


n = int(input("Enter your birth year: "))
res = calc_age(n)
print("Your age: ", res)

