from itertools import *


a = []
for i in product('ГЕПАРД', repeat=5):
    s = ''.join(i)
    if s.count('Г') == 1 and s[0] != 'А' and s[-1] != 'Е':
        a.append(s)
print(4*3*5*5*4 + 1*5*5*5*4 + 4*5*5*5*1)
print(len(a))