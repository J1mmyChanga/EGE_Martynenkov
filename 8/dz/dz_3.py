from itertools import *


a = []
for i in product('ПУЛЯ', repeat=6):
    s = ''.join(i)
    if s.count('У') == 2:
        a.append(s)
print(6*5/2*3**4)
print(len(a))