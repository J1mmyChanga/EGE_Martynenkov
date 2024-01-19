from itertools import *

data = sorted(list(''.join(i) for i in product('АЕКПТЧ', repeat=7)))
print(data.index('АПТЕЧКА'))
print(data.index('ПЕЧАТКА'))