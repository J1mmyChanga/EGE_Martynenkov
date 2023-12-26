from itertools import product, permutations

def f(x, y, z, w):
    return (y <= (x or z)) and (z <= y)

table = [(1, 0, 0, 0), (1, 1, 0, 0), (1, 1, 0, 1), (0, 1, 1, 0)]
for p in permutations('xyzw'):
    if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0, 0]:
        print(p)