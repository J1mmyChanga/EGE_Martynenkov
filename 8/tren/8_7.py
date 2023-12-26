from itertools import *


a = []
for i in product('ЗЕРКАЛО', repeat=6):
    s = ''.join(i)
    if s.count('К') == 1 and s.count('А') == 3:
        a.append(s)
print(len(a))