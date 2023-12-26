from itertools import product, permutations

def f(x, y, z, w):
    return (not y) and x and ((not z) or w)

table = [(0, 1, 0, 0), (1, 1, 0, 0), (1, 1, 1, 0)]
for p in permutations('xyzw'):
    if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
        print(p)