
# Program that reads data from a csv file and prints it in the console
import csv

with open('file5.csv', 'w', newline='') as file:  # Writing data in the csv file
    writer = csv.writer(file)
    writer.writerow(["EmpID", "EmpName", "Salary", "Department"])  # headings of csv file
    writer.writerow([101, "Ajay", 10000, "Marketing"])  # Inputs
    writer.writerow([102, "Reema", 12000, "Product"])
    writer.writerow([103, "Samar", 8000, "Marketing"])

with open('file5.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';', skipinitialspace=True)
    for row in reader:
        print(row)
