from itertools import *


a = []
for i in product('WXYZ', 'ABC', 'ABC', 'ABC', 'ABC', 'WXYZ',):
    s = ''.join(i)
    a.append(s)
print(4**2*3**4)
print(len(a))