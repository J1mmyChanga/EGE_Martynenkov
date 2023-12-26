from itertools import *


a = []
for i in permutations('ДЕЙКСТРА', 6):
    s = ''.join(i)
    if s.count('Й') == 1:
        s = s.replace('Д', 'К').replace('С', 'К').replace('Т', 'К').replace('Р', 'К')
        if 'ЙК' in s:
            a.append(s)
print(5*5*6*5*4*3)
print(len(a))