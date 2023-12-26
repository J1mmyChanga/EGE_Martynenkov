from itertools import *


a = []
for i in product('БЕРКЛИЙ', repeat=4):
    s = ''.join(i)
    if (s.count('Е') >= 1 or s.count('И') >= 1) and not s.startswith('Й'):
        a.append(s)
print(len(a))