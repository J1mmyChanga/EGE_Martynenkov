from itertools import *

d = {}

combs = list(product('0123456789', repeat=3)) + list(product('0123456789', repeat=2)) + list(product('0123456789', repeat=1)) + ['']

for x in range(10):
    for y in combs:
        y = ''.join(y)
        if int(f'123{x}4{y}5679') % 4013 == 0:
            d[f'123{x}4{y}5679'] = int(f'123{x}4{y}5679') / 4013
print(*d.items(), sep='\n')