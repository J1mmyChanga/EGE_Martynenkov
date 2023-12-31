from itertools import permutations

def f(x, y, z, w):
    return (not y) or x or ((not z) and w)

table = [(0, 0, 0, 1), (0, 0, 1, 1), (1, 0, 1, 1)]
for p in permutations('xyzw'):
    if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
        print(p)