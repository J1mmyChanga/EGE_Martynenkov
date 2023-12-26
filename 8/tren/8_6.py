from itertools import *


a = []
for i in product('КАНТ', repeat=6):
    s = ''.join(i)
    if s.count('К') == 2:
        a.append(s)
print(len(a))