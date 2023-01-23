import csv

file = open('Salary_Data.csv')
csvreader = csv.reader(file)

header = []
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

print(header)
print(rows)

file.close()