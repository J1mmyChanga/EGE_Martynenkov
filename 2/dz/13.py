from itertools import product, permutations

def f(x, y, z, w):
    return ((w <= y) or (not(y <= z))) and (not x) and (not(x == z))

for item in product([0, 1], repeat=5):
    table = [(0, item[0], 1, item[1]), (1, item[2], item[3], 1), (0, item[4], 1, 1)]
    if len(set(table)) != len(table):
        continue
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
            print(p)