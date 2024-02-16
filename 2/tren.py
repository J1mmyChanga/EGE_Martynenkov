from itertools import *

def f(x, y, z, w):
    return y and (x or z) or (not (y or z)) or w

for item in product([0, 1], repeat=4):
    table = [(1, item[0], 0, 1), (item[1], 1, 0, item[2]), (0, 0, item[3], 1)]
    if len(table) != len(set(table)):
        continue
    for p in permutations('wxyz'):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(p)