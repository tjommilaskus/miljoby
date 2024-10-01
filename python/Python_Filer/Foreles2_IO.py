import csv
import math

filename = "test.csv"
list1 = [1,2,3,4,5,6]
list2 = [x * x for x in list1]

# Create and write to a file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(list1)
    writer.writerow(list2)

#read from a file
with open(filename, 'r') as file:
    rows = csv.reader(file)
    list2a = next(rows)
    list2b= next(rows)


print (list2a)
print (list2b)

from datetime import date
d0 = date(2024, 1, 1)
d1 = date(2024, 4, 1)
delta = d1 - d0
print(delta.days)





