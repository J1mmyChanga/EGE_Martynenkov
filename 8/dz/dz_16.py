from itertools import *


a = []
for i in permutations('ВАЙФУ', 4):
    s = ''.join(i)
    if s[0] != 'Й' and 'ВФ' not in s and 'ФВ' not in s:
        a.append(s)
print(5*5*6*5*4*3)
print(len(a))