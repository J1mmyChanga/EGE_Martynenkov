from itertools import product, permutations

def f(x, y, z, w):
    return (x == (not z)) <= ((x or w) == y)

for item in product([0, 1], repeat=5):
    table = [(0, item[0], 0, item[1]), (item[2], item[3], 0, 0), (item[4], 0, 0, 0)]
    if len(set(table)) != len(table):
        continue
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(p)