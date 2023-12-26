from itertools import product, permutations

def f(x, y, z, w):
    return (((not x) and y) == z) and w

for item in product([0, 1], repeat=10):
    table = [(item[0], 0, item[1], item[2]), (item[3], item[4], item[5], 0), (0, 0, item[6], item[7]), (0, 0, item[8], item[9])]
    if len(set(table)) != len(table):
        continue
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1, 1]:
            print(p)