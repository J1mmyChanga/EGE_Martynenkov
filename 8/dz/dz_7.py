from itertools import *


a = []
for i in permutations('АБИКОЛУН', 8):
    s = ''.join(i).replace('И', 'А').replace('О', 'А').replace('У', 'А')\
    .replace('К', 'Б').replace('Л', 'Б').replace('Н', 'Б')
    if 'АА' not in s and 'ББ' not in s:
        a.append(s)
        print(s)
print(4*4*3*3*2*2*2)
print(len(a))