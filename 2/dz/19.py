from itertools import product, permutations

def f(x, y, z, w):
    return (x and z) or ((w <= x) == (z <= y))

for item in product([0, 1], repeat=6):
    table = [(item[0], item[1], item[2], 1), (item[3], item[4], 1, 1), (item[5], 1, 1, 1)]
    if len(set(table)) != len(table):
        continue
    for k, p in enumerate(permutations('xyzw')):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(p)