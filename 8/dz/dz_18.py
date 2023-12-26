from itertools import *


a = []
for i in product('ЛЕМУР', repeat=4):
    s = ''.join(i)
    a.append(s)
a = sorted(a)
for i in range(len(a)):
    if a[i][0] == 'Л':
        print(i + 1)
        break