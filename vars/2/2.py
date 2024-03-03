from itertools import *

def f(x, y, z, w):
    return (x or y or z) <= (x and (y or w))

for i in product([0,1], repeat=4):
    table = [(1, 0, i[0], 0), (i[1], 1, 1, i[2]), (1, 1, i[3], 1)]
    if len(set(table)) != len(table):
        continue
    for i in permutations('xyzw'):
        if [f(**dict(zip(i, row))) for row in table] == [0, 0, 0]:
            print(i)