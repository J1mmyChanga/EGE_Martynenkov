from itertools import *


a = []
for i in product('КМ', 'КУМА', 'КУМА', 'КУМА', 'УА'):
    s = ''.join(i)
    a.append(s)
print(len(a))