from itertools import product, permutations

def f(x, y, z, w):
    return ((z <= x) and (x <= w)) or (y == (z or x))

for item in product([0, 1], repeat=7):
    table = [(item[0], 1, item[1], item[2]), (item[3], item[4], 1, 1), (item[5], 1, item[6], 1)]
    if len(set(table)) != len(table):
        continue
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(p)