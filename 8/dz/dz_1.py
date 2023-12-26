from itertools import *


a = []
for i in product('КРСЛ', 'КРЕСЛО', 'КРЕСЛО', 'ЕО'):
    s = ''.join(i)
    a.append(s)
print(4*6*6*2)
print(len(a))