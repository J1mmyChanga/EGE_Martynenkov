from itertools import *


a = []
for i in product('САЛО', repeat=6):
    s = ''.join(i)
    if 0 < s.count('О') <= 3:
        a.append(s)
print(6*3**5 + 6*5/2*3**4 + 6*5*4/6*3**3)
print(len(a))