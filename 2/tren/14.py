from itertools import permutations, product


def f(x, y, z, w):
    return ((y <= x) or ((not z) and w)) == (w == x)

for item in product([0, 1], repeat=3):
    table = [(item[0], 1, 0, 0), (0, 0, 0, 1), (0, 1, item[1], item[2])]
    if len(table) != len(set(table)):
        continue
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
            print(p)