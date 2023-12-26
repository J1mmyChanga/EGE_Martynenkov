from itertools import *


a = []
pred = 0
for i in product('АЛГОРИТМ', repeat=4):
    s = ''.join(i)
    a.append(s)
a = sorted(a)
for i in range(len(a)):
    if a[i][-2:] == 'ИМ':
        pred = i + 1
print(pred)