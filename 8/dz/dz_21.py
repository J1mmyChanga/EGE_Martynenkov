from itertools import *


a = []
for i in product('МАРИЯ', repeat=4):
    s = ''.join(i)
    a.append(s)
a = sorted(a)
print(a[210])