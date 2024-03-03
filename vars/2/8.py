from itertools import *

c = 0
for i in permutations('РЕЖИМДНО', r=6):
    i = ''.join(i).replace('И', 'Е').replace('О', 'Е').replace('Ж', 'Р').replace('М', 'Р').replace('Д', 'Р').replace('Н', 'Р')
    if i[:2] == 'РЕ' and i[-1] == 'Е':
        c += 1
print(c)