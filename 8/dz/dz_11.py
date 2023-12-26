from itertools import *


a = []
for i in product('ВИШНЯ', repeat=6):
    s = ''.join(i)
    if s.count('В') <= 1 and s[0] != 'Ш' and s[-1] not in 'ИЯ':
        a.append(s)
print(3*4*4*4*4*2*2 + 1*4*4*4*4*2 + 3*4*4*4*4*1)
print(len(a))