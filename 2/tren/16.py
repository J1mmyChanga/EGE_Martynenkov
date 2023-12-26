from itertools import permutations, product


def f(x, y, z, w):
    return ((x <= z) <= y) or (not w)

for item in product([0, 1], repeat=7):
    table = [(1, 0, item[0], item[1]), (item[2], 1, 0, item[3]), (0, item[4], item[5], item[6])]
    if len(table) != len(set(table)):
        continue
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(p)