from itertools import *


a = []
for i in product('КРОТ', repeat=6):
    s = ''.join(i)
    if s.count('О') == 1:
        a.append(s)
print(len(a))