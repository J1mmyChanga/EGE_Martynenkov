from itertools import *


a = []
for i in product('ЛЕТО', repeat=4):
    s = ''.join(i)
    if s.count('Е') >= 1:
        a.append(s)
print(len(a))