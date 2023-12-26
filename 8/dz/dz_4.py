from itertools import *


a = []
for i in product('ЛОДКА', repeat=4):
    s = ''.join(i)
    if s.count('О') >= 2:
        a.append(s)
print(5**4 - 4**4 - 4**4)
print(len(a))