from itertools import *
c = 0

def f(x, y, z, w):
    return (y or x) == ((y <= w) or (not z))

table = [(1, 0, 0, 0), (0, 1, 0, 0), (1, 0, 1, 0)]
for p in permutations('xyzw'):
    if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
        print(p)