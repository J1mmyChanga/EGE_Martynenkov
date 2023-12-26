from itertools import *


a = []
res = list(product('АНИМЕ', repeat=6)) + list(product('АНИМЕ', repeat=5)) + list(product('АНИМЕ', repeat=4))
for i in res:
    s = ''.join(i)
    a.append(s)
print(len(a))