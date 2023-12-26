from itertools import *


a = []
for i in product('ЛТ', 'ЛЕТО', 'ЛЕТО', 'ЛЕТО'):
    s = ''.join(i)
    a.append(s)
print(len(a))