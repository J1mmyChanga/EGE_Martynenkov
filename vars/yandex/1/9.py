import csv
from itertools import *

c = 0
with open('9.csv', 'r', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=';', quoting=csv.QUOTE_ALL)
    for i in list(data):
        if any(int(x) + int(y) == int(z) + int(w) == 180 for x, y, z, w in combinations(i, 4)):
            c += 1
print(c)