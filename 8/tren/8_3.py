from itertools import *


a = []
for i in product('ABC', 'ABC', 'ABC', 'ABC', 'ABCX'):
    s = ''.join(i)
    a.append(s)
print(len(a))