from itertools import permutations, product


def f(x, y, z, w):
    return (x == (not y)) <= ((x and w) == z)

for item in product([0, 1], repeat=5):
    table = [(1, 1, item[0], item[1]), (1, 1, item[2], 1), (item[3], 1, 1, item[4])]
    if len(table) != len(set(table)):
        continue
    for p in permutations('xyzw'):
        print(p)
        if [f(**dict(zip(p, row))) for row in table] == [0, 0, 0]:
            print(p)