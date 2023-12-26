from itertools import *


a = []
for i in product('AB123', repeat=8):
    s = ''.join(i)
    if s.count('A') + s.count('B') == 2:
        a.append(s)
print(8*7/2*4*3**6)
print(len(a))