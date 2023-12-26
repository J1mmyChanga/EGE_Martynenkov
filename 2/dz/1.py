from itertools import product, permutations

def f(x, y, z, w):
    return (x or (not y)) and (not (y == z)) and w

for item in product([0, 1], repeat=4):
    table = [(0, 1, item[0], 0), (item[1], 1, 1, 0), (1, item[2], 0, item[3])]
    if len(set(table)) != len(table):
        continue
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
            print(p)