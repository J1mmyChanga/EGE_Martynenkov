from itertools import *


a = []
for i in product('ЭЮЯ', 'АБВГ', 'АБВГ', 'АБВГ', 'ЭЮЯ'):
    s = ''.join(i)
    a.append(s)
print(len(a))