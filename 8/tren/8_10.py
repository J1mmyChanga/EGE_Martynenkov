from itertools import *


a = []
for i in product('КАТЕР', repeat=3):
    s = ''.join(i)
    if s.count('Р') >= 2:
        a.append(s)
print(len(a))