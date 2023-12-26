from itertools import *


a = []
for i in permutations('ИГРОК', 5):
    s = ''.join(i)
    if s[0] != 'К' and 'РОК' not in s:
        a.append(s)
print(2*3*4*5 - 4*3*2 - 3*2)
print(len(a))