from itertools import product, permutations

def f(x, y, z, w):
    return (x and (not y)) or (x == z) or w

for item in product([0, 1], repeat=6):
    table = [(1, item[0], item[1], 1), (item[2], 0, item[3], 0), (1, item[4], 1, item[5])]
    if len(set(table)) != len(table):
        continue
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(p)