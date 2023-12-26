from itertools import product, permutations

def f(x, y, z, w):
    return (y <= x) or (not ((x <= z) and (z <= x))) and (not w)

for item in product([0, 1], repeat=6):
    table = [(0, 0, 0, item[0]), (item[1], 0, 0, item[2]), (item[3], item[4], 0, item[5])]
    if len(set(table)) != len(table):
        continue
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(p)