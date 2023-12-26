from itertools import *


a = []
for i in product('01234', repeat=6):
    s = ''.join(i)
    if s[0] != '0' and s[0] != '1' and s[-1] != '3' and s[-1] != '4':
        a.append(s)
print(3*5**4*3)
print(len(a))